import requests

from domain.i_obtain_booking_references import IObtainBookingReferences
from domain.train_info import BookingReference


class BookingReferenceService(IObtainBookingReferences):
    def __init__(self):
        self._base_url = 'http://localhost:8082/booking_reference/'

    def obtain_booking_reference(self) -> BookingReference:
        response = requests.get(self._base_url)
        return response.text
