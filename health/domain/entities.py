"""Domain entities for the Health-bounded context"""
from datetime import datetime


class HealthRecord:
    """Represents a Health Record entity in the Health context.

    Attributes:
        id (int): Unique identifier for the health record.
        device_id (str): Identifier for the device that recorded the health data.
        bpm (float): Beats per minute recorded by the device.
        created_at (datetime): Timestamp when the record was created.
    """
    def __init__(self, device_id: str, bpm: float, created_at: datetime, id: int = None):
        """Initialize a HealthRecord instance.

        Args:
            device_id (str): Identifier for the device that recorded the health data.
            bpm (float): Beats per minute recorded by the device.
            created_at (datetime): Timestamp when the record was created.
            id (int, optional): Unique identifier for the health record. Defaults to None.
        """
        self.id = id
        self.device_id = device_id
        self.bpm = bpm
        self.created_at = created_at