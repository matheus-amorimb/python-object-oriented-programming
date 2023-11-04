import numbers
from datetime import datetime, timezone, timedelta

class TimeZone():
    def __init__(self, offset_name = 'UTC', offset_hours=0):
        if not offset_name.isalpha():
            raise ValueError('Timezone name must contain only letters and cannot be empty.')
        
        if not isinstance(offset_hours, numbers.Integral):
            raise ValueError('Hour offset must be an integer.')

        if offset_hours < -12 or offset_hours > 14:
            raise ValueError('Offset must be between -12:00 and +14:00')

        offset = timedelta(hours=offset_hours)
        self._name = offset_name
        self._offset = offset
        
    @property
    def offset(self):
        return self._offset
    
    @property
    def name(self):
        return self._name

if __name__ == "__main__":
    pass