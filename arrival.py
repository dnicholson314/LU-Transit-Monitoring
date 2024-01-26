class Arrival:
    def __init__(self, route_id: int, vehicle_id: int, stop: str, seconds: int):
        self.route_id = route_id
        self.vehicle_id = vehicle_id
        self.stop = stop
        self.seconds = seconds if seconds > 0 else 0

    def get_mins(self) -> int:
        return self.seconds // 60