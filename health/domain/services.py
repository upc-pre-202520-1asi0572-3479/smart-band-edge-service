"""Domain services for the Health context."""
from datetime import datetime, timezone

from dateutil.parser import parse

from health.domain.entities import HealthRecord


class HealthRecordService:
    def __init__(self):
        """
        Initialize the HealthRecordService.
        """
        pass

    @staticmethod
    def create_record(device_id: str, bpm: float, created_at: str | None)->HealthRecord:
        """
        Create a HealthRecord entity after validating the input data.
        :param device_id: The ID of the device.
        :param bpm: Beats per minute.
        :param created_at: Timestamp of the record creation in ISO 8601 format.
        :return: A HealthRecord entity.
        :raises ValueError: If the input data is invalid.
        """
        try:
            bpm = float(bpm)
            if not (0 <= bpm <= 200):
                raise ValueError("BPM must be between 0 and 200.")
            if created_at:
                parsed_created_at = parse(created_at).astimezone(timezone.utc)
            else:
                parsed_created_at = datetime.now(timezone.utc)
        except (ValueError, TypeError):
            raise ValueError("Invalid data format.")

        return HealthRecord(device_id, bpm, parsed_created_at)


