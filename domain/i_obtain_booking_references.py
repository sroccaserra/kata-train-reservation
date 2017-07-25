from abc import ABC, abstractmethod

from domain.train_info import BookingReference


class IObtainBookingReferences(ABC):
    @abstractmethod
    def obtain_booking_reference(self) -> BookingReference:
        pass
