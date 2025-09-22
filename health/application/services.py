"""Application services for Health context."""
from health.domain.entities import HealthRecord
from health.domain.services import HealthRecordService
from health.infrastructure.repositories import HealthRecordRepository
from iam.infrastructure.repositories import DeviceRepository


class HealthRecordApplicationService:
    """
    Application service for managing health records.
    """
    def __init__(self):
        """
        Initializes the HealthRecordApplicationService with necessary repositories and services.
        """
        self.health_record_repository = HealthRecordRepository()
        self.health_record_service = HealthRecordService()
        self.device_repository = DeviceRepository()

    def create_health_record(self, device_id: str, bpm: float, created_at: str, api_key: str)->HealthRecord:
        """
        Creates a health record after validating the device and API key.
        :param device_id: The ID of the device
        :param bpm: Beats per minute
        :param created_at: Timestamp of the record creation
        :param api_key: API key for device authentication
        :return: HealthRecord: The created health record
        :raises ValueError: If the device is not found or the API key is invalid
        """
        if not self.device_repository.find_by_id_and_api_key(device_id, api_key):
            raise ValueError("Device not found or invalid API key")
        record = self.health_record_service.create_record(device_id, bpm, created_at)
        return self.health_record_repository.save(record)