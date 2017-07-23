from unittest import TestCase

from domain.train_data import TrainData
from domain.i_obtain_train_data import NO_BOOKING_REFERENCE
from test.common import TEST_BOOKING_REFERENCE


class TestTrainData(TestCase):
    def test_capacity_of_empty_train_for_10_seats(self):
        train_data = TrainData(make_raw_train_data(seats=10))

        self.assertEqual(7,
                         train_data.remaining_capacity())

    def test_capacity_of_empty_train_for_100_seats(self):
        train_data = TrainData(make_raw_train_data(seats=100))

        self.assertEqual(70,
                         train_data.remaining_capacity())

    def test_capacity_of_train_of_10_seats_and_one_reserved_seat(self):
        train_data = TrainData(make_raw_train_data(seats=10,
                                                   reserved_seats=1,
                                                   booking_reference=TEST_BOOKING_REFERENCE))

        self.assertEqual(6,
                         train_data.remaining_capacity())

    def test_free_seat_count_of_an_empty_train_of_10_seats(self):
        train_data = TrainData(make_raw_train_data(seats=10))

        self.assertEqual(10,
                         train_data.free_seat_count())

    def test_free_seat_count_of_train_of_10_seats_and_one_reserved_seat(self):
        train_data = TrainData(make_raw_train_data(seats=10,
                                                   reserved_seats=1,
                                                   booking_reference=TEST_BOOKING_REFERENCE))

        self.assertEqual(9,
                         train_data.free_seat_count())


def make_raw_train_data(seats, reserved_seats=0, booking_reference=NO_BOOKING_REFERENCE):
    return {
        'seats': {
            '{0}A'.format(x):
                make_seat_raw_data(x) if x > reserved_seats
                else make_seat_raw_data(x, booking_reference=booking_reference)
            for x in range(1, seats + 1)
        }
    }


def make_seat_raw_data(seat_number, booking_reference=NO_BOOKING_REFERENCE):
    return {
        'booking_reference': booking_reference,
        'seat_number': str(seat_number),
        'coach': 'A'
    }
