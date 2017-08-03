from unittest import TestCase

from pytest import mark

from infrastructure.service_providers.booking_reference_service import BookingReferenceService


@mark.integration
class TestBookingReferenceService(TestCase):
    def test_building_train_info(self):
        # Given
        booking_reference_service = BookingReferenceService()
        # When
        booking_reference = booking_reference_service.obtain_booking_reference()
        # Then
        self.assertEqual(7, len(booking_reference))
