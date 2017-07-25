import math

from typing import NewType

BookingReference = NewType('BookingReference', str)
TrainId = NewType('TrainId', str)

NO_BOOKING_REFERENCE: BookingReference = ''


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

    def get_some_free_seat_ids(self, seat_count):
        free_seats = self._free_seats()
        return [_site_id(seat) for seat in free_seats[:seat_count]]

    def _free_seats(self):
        return [raw_seat for raw_seat in self._raw_seats_data if
                _is_free(raw_seat)]


def _site_id(raw_seat):
    return raw_seat['seat_number'] + raw_seat['coach']


def _is_free(raw_seat):
    return raw_seat['booking_reference'] == NO_BOOKING_REFERENCE
