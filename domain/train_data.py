from domain.train_data_service import NO_BOOKING_REFERENCE


class TrainData:
    def __init__(self, raw_train_data):
        self.raw_train_data = raw_train_data

    def raw_seats(self):
        return self.raw_train_data['seats'].values()

    def total_seat_count(self):
        seats = self.raw_train_data['seats']
        return len(seats)

    def total_capacity(self):
        return self.total_seat_count() * 70 / 100

    def remaining_capacity(self):
        return self.total_capacity() - (self.total_seat_count() - self.free_seat_count())

    def free_seat_count(self):
        free_seats = [raw_seat for raw_seat in self.raw_seats() if
                      is_free(raw_seat)]
        return len(free_seats)


def is_free(raw_seat):
    return raw_seat['booking_reference'] == NO_BOOKING_REFERENCE
