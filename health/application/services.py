"""Application services for Health context."""
from health.domain.services import HealthRecordService
from health.infrastructure.repositories import HealthRecordRepository


class HealthRecordApplicationService:
    def __init__(self):
        self.health_record_repository = HealthRecordRepository()
        self.health_record_service = HealthRecordService()
        """TODO: Initialize device repository"""