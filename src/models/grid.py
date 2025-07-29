import time, math
from pydantic import BaseModel
from src.models.vector import Vector3


class LocalGrid(BaseModel):
    model_config = {"extra": "ignore"}
    """
    # MAKE SURE UNITS ARE THE SAME
    Local Grid is a coordinate system that rotates around a point in space.
    """
    origin: Vector3
    rotation_speed_hours: float  
    initial_time: float  =  time.time()
    initial_local_point: Vector3  
    initial_global_point: Vector3  # usually from clipboard so in m, rest is displayed in km usually
    


    @property
    def rotation_speed(self) -> float:
        return self._hours_to_rad_per_sec(self.rotation_speed_hours)
    def asglobal(self, vector: Vector3, current_time: float) -> Vector3:
        """Convert a local vector at current_time to global coordinates."""
        phi = self._current_angle(current_time)
        cos_phi = math.cos(phi)
        sin_phi = math.sin(phi)
        # rotate
        x_rot = vector.x * cos_phi - vector.y * sin_phi
        y_rot = vector.x * sin_phi + vector.y * cos_phi
        z_rot = vector.z
        # translate
        return Vector3(
            x=x_rot + self.origin.x,
            y=y_rot + self.origin.y,
            z=z_rot + self.origin.z
        )
    def aslocal(self, vector: Vector3, current_time: float) -> Vector3:
        """Convert a global vector at current_time to local coordinates."""
        # subtract origin
        v = Vector3(
            x=vector.x - self.origin.x,
            y=vector.y - self.origin.y,
            z=vector.z - self.origin.z
        )
        phi = self._current_angle(current_time)
        cos_phi = math.cos(phi)
        sin_phi = math.sin(phi)
        # rotate by -phi
        x_loc = -v.x * cos_phi + v.y * sin_phi
        y_loc = -v.x * sin_phi + v.y * cos_phi
        z_loc = v.z
        return Vector3(x=x_loc, y=y_loc, z=z_loc)    
    def _initial_angle(self) -> float:
        # Compute initial frame twist phi0 = arg(R) - arg(local)
        R = self.initial_global_point - self.origin
        phi_r = math.atan2(R.y, R.x)
        phi_l = math.atan2(self.initial_local_point.y, self.initial_local_point.x)
        return phi_r - phi_l
    def _current_angle(self, current_time: float) -> float:
        dt = current_time - self.initial_time
        return self._initial_angle() + self.rotation_speed * dt    
    def _period_to_rad_per_sec(self, period_seconds: float) -> float:
        """
        Convert a rotation period (full rotation) given in seconds into angular speed in radians per second.
        """
        if period_seconds <= 0:
            raise ValueError("Period must be positive")
        return 2 * math.pi / period_seconds
    def _hours_to_rad_per_sec(self, hours: float) -> float:
        """
        Convert a rotation period given in hours into angular speed (rad/s).
        """
        return self._period_to_rad_per_sec(hours * 3600)
