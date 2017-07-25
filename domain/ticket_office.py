from domain.i_obtain_booking_references import IObtainBookingReferences
from domain.i_obtain_train_info import IObtainTrainInfo
from domain.train_info import NO_BOOKING_REFERENCE, TrainId


class TicketOffice:
    def __init__(self, train_info_service: IObtainTrainInfo,
                 booking_reference_service: IObtainBookingReferences):
        self._train_info_service = train_info_service
        self._booking_reference_service = booking_reference_service

    def reserve(self, train_id: TrainId, seat_count):
        train_info = self._train_info_service.obtain_info_for_train(train_id)

        if not train_info.can_reserve_seats(seat_count):
            return _empty_reservation(train_id)

        booking_reference = self._booking_reference_service.obtain_booking_reference()
        seat_ids = train_info.get_some_free_seat_ids(seat_count)

        return {
            'train_id': train_id,
            'booking_reference': booking_reference,
            'seats': seat_ids
        }


def _empty_reservation(train_id: TrainId):
    return {
        'train_id': train_id,
        'booking_reference': NO_BOOKING_REFERENCE,
        'seats': []
    }
