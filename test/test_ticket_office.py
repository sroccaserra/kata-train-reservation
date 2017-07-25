from unittest import TestCase
from unittest.mock import Mock

from domain.i_obtain_booking_references import IObtainBookingReferences
from domain.i_obtain_train_info import IObtainTrainInfo
from domain.ticket_office import TicketOffice
from domain.train_info import TrainInfo, NO_BOOKING_REFERENCE
from test.common import TRAIN_ID, TEST_BOOKING_REFERENCE
from test.test_train_info import build_seats_data


class TrainsWithOneCoach(TestCase):
    def setUp(self):
        self.train_data_service = Mock(IObtainTrainInfo)
        self.train_data_service.obtain_info_for_train.return_value = \
            TrainInfo(build_seats_data(total_seats=10))

        self.booking_reference_service = Mock(IObtainBookingReferences)
        self.booking_reference_service.obtain_booking_reference.return_value = \
            TEST_BOOKING_REFERENCE

        # noinspection PyTypeChecker
        self.ticket_office = TicketOffice(self.train_data_service,
                                          self.booking_reference_service)

    def test_can_reserve_one_seat_in_empty_coach(self):
        reservation = self.ticket_office.reserve(TRAIN_ID, 1)

        self.assertEqual(TRAIN_ID, reservation['train_id'])
        self.assertEqual(TEST_BOOKING_REFERENCE, reservation['booking_reference'])
        self.assertEqual(['1A'], reservation['seats'])

    def test_can_reserve_two_seats_in_empty_coach(self):
        reservation = self.ticket_office.reserve(TRAIN_ID, 2)

        self.assertEqual(['1A', '2A'],
                         reservation['seats'])

    def test_cant_reserve_one_seat_in_max_capacity_coach(self):
        self.train_data_service.obtain_info_for_train.return_value = \
            TrainInfo(build_seats_data(total_seats=10,
                                       reserved_seats=7,
                                       booking_reference=TEST_BOOKING_REFERENCE))

        reservation = self.ticket_office.reserve(TRAIN_ID, 1)

        self.assertEqual(build_empty_reservation(),
                         reservation)

    def test_booking_reference_is_obtained(self):
        other_booking_reference = 'dabbad00'
        self.booking_reference_service.obtain_booking_reference.return_value = \
            other_booking_reference

        reservation = self.ticket_office.reserve(TRAIN_ID, 1)

        self.assertEqual(other_booking_reference,
                         reservation['booking_reference'])


def build_empty_reservation():
    return {
        'train_id': TRAIN_ID,
        'booking_reference': NO_BOOKING_REFERENCE,
        'seats': []
    }
