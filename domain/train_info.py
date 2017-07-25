import math

NO_BOOKING_REFERENCE = ''


class TrainInfo:
    def __init__(self, raw_seats_data):
        self._raw_seats_data = raw_seats_data
        self._total_seat_count = len(self._raw_seats_data)
        self._max_capacity = math.floor((self._total_seat_count * 70) / 100)

    def reserved_seat_count(self):
        free_seats = self._free_seats()
        free_seat_count = len(free_seats)
        return self._total_seat_count - free_seat_count

    def can_reserve_seats(self, seat_count) -> bool:
        return self._max_capacity >= self.reserved_seat_count() + seat_count

    def get_some_free_seats(self, seat_count):
        free_seats = self._free_seats()
        return [seat['seat_number'] + seat['coach'] for seat in free_seats[:seat_count]]

    def _free_seats(self):
        return [raw_seat for raw_seat in self._raw_seats_data if
                is_free(raw_seat)]


def is_free(raw_seat):
    return raw_seat['booking_reference'] == NO_BOOKING_REFERENCE
