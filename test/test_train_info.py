from unittest import TestCase

from domain.train_info import TrainInfo, NO_BOOKING_REFERENCE
from test.common import TEST_BOOKING_REFERENCE


class TestTrainInfoRemainingCapacity(TestCase):
    def test_remaining_capacity_of_empty_train_for_10_seats(self):
        train_info = TrainInfo(build_seats_data(total_seats=10))

        self.assertTrue(train_info.can_reserve_seats(7))
        self.assertFalse(train_info.can_reserve_seats(8))

    def test_remaining_capacity_of_empty_train_for_100_seats(self):
        train_info = TrainInfo(build_seats_data(total_seats=100))

        self.assertTrue(train_info.can_reserve_seats(70))
        self.assertFalse(train_info.can_reserve_seats(71))

    def test_remaining_capacity_of_train_of_10_seats_and_one_reserved_seat(self):
        train_info = TrainInfo(build_seats_data(total_seats=10,
                                                reserved_seats=1,
                                                booking_reference=TEST_BOOKING_REFERENCE))

        self.assertTrue(train_info.can_reserve_seats(6))
        self.assertFalse(train_info.can_reserve_seats(7))


class TestTrainInfoReservedSeats(TestCase):
    def test_reserved_seat_count_of_an_empty_train_of_10_seats(self):
        train_info = TrainInfo(build_seats_data(total_seats=10))

        self.assertEqual(0, train_info.reserved_seat_count())

    def test_reserved_seat_count_of_train_of_10_seats_and_one_reserved_seat(self):
        train_info = TrainInfo(build_seats_data(total_seats=10,
                                                reserved_seats=1,
                                                booking_reference=TEST_BOOKING_REFERENCE))

        self.assertEqual(1, train_info.reserved_seat_count())


class TestTrainInfoFreeSeats(TestCase):
    def test_free_seats_in_empty_train(self):
        train_info = TrainInfo(build_seats_data(total_seats=10))

        self.assertEqual(['1A'], train_info.get_some_free_seat_ids(1))
        self.assertEqual(['1A', '2A'], train_info.get_some_free_seat_ids(2))

    def test_free_seats_in_non_empty_train(self):
        train_info = TrainInfo(build_seats_data(total_seats=10,
                                                reserved_seats=1,
                                                booking_reference=TEST_BOOKING_REFERENCE))

        self.assertEqual(['2A'], train_info.get_some_free_seat_ids(1))
        self.assertEqual(['2A', '3A'], train_info.get_some_free_seat_ids(2))


def build_seats_data(total_seats, reserved_seats=0, booking_reference=NO_BOOKING_REFERENCE):
    return [
        build_seat_data(x) if x > reserved_seats
        else build_seat_data(x, booking_reference=booking_reference)
        for x in range(1, total_seats + 1)
    ]


def build_seat_data(seat_number, booking_reference=NO_BOOKING_REFERENCE):
    return {
        'booking_reference': booking_reference,
        'seat_number': str(seat_number),
        'coach': 'A'
    }
