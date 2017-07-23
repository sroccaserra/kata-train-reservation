from domain.i_obtain_train_data import NO_BOOKING_REFERENCE


class TicketOffice:
    def __init__(self, train_data_service, booking_reference_service):
        self.train_data_service = train_data_service
        self.booking_reference_service = booking_reference_service

    def reserve(self, train_id, seat_count):
        train_data = self.train_data_service.obtain_data_for_train(train_id)

        if train_data.remaining_capacity() < seat_count:
            booking_reference = NO_BOOKING_REFERENCE
            seats = []
        else:
            booking_reference = self.booking_reference_service.obtain_booking_reference()
            seats = ['{0}A'.format(x) for x in range(1, seat_count + 1)]

        return {
            'train_id': train_id,
            'booking_reference': booking_reference,
            'seats': seats
        }
