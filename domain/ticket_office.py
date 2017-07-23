class TicketOffice:
    def reserve(self, train_id, seat_count):
        booking_reference = '75bcd15'
        seats = ['{0}A'.format(x) for x in range(1, seat_count + 1)]

        return {
            'train_id': train_id,
            'booking_reference': booking_reference,
            'seats': seats
        }
