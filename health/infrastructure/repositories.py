"""
Repositories for health-related data management.
"""
from health.domain.entities import HealthRecord
from health.infrastructure.models import HealthRecord as HealthRecordModel


class HealthRecordRepository:
    """
    Repository for managing HealthRecord entities.
    """
    @staticmethod
    def save(health_record)->HealthRecord:
        """
        Save a HealthRecord entity to the database.
        :param health_record: HealthRecord entity to be saved.
        :return:
        HealthRecord: The saved HealthRecord entity with updated ID.
        """
        record = HealthRecordModel.create(
            device_id = health_record.device_id,
            bpm = health_record.bpm,
            created_at = health_record.created_at
        )
        return HealthRecord(
            health_record.device_id,
            health_record.bpm,
            health_record.created_at,
            record.id
        )

