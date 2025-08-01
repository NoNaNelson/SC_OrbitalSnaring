from src.models.planet import Planet
from src.models.vector import Vector3

def orbital_pos_verification(x, y, z,
                             start_om: Vector3, end_om: Vector3
                             ):
    try:
        directionalvector = start_om - end_om
        POS= Vector3(x, y, z)
        d = ((start_om - POS).dot(directionalvector)) / directionalvector.len
        print(f"Distance to selected route: {abs(d):.2f}m")
        return True
    except Exception as e:
        print(f"Error in orbital position verification: {e}")
        return False