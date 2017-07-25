import math

NO_BOOKING_REFERENCE = ''


class TrainInfo:
    def __init__(self, raw_train_data):
        self._raw_seats = raw_train_data['seats'].values()
        self._total_seat_count = len(self._raw_seats)
        self._max_capacity = math.floor((self._total_seat_count * 70) / 100)

    def reserved_seat_count(self):
        free_seats = [raw_seat for raw_seat in self._raw_seats if
                      is_free(raw_seat)]

        free_seat_count = len(free_seats)
        return self._total_seat_count - free_seat_count

    def can_reserve_seats(self, seat_count):
        return self._max_capacity >= self.reserved_seat_count() + seat_count


def is_free(raw_seat):
    return raw_seat['booking_reference'] == NO_BOOKING_REFERENCE
