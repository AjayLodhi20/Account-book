import numbers
from datetime import timedelta

class TimeZone():
    def __init__(self, name, offset_hours, offset_minutes):
        if name is None or len(str(name).strip())=0:
            raise ValueError("Timezone cannot be empty.")

        self._name = str(name).strip()

        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError("Hour offset must be an integer.")
        if not isinstance(offset_minutes, numbers.Integral):
            raise ValueError("Minutes offset must be an integer.")

        if offset_minutes > 59 or offset_minutes < -59:
            raise ValueError("minutes offset must be between -59 and 59")