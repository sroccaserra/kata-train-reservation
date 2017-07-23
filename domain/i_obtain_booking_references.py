from abc import ABC, abstractmethod


class IObtainBookingReferences(ABC):
    @abstractmethod
    def obtain_booking_reference(self):
        pass
