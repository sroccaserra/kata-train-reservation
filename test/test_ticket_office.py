from unittest import TestCase
from unittest.mock import Mock

from domain.i_obtain_booking_references import IObtainBookingReferences
from domain.ticket_office import TicketOffice
from domain.train_data import TrainData
from domain.i_obtain_train_data import IObtainTrainData, NO_BOOKING_REFERENCE
from test.common import TRAIN_ID, TEST_BOOKING_REFERENCE
from test.test_train_data import make_raw_train_data


class TrainsWithOneCoach(TestCase):
    def setUp(self):
        self.train_data_service = Mock(IObtainTrainData)
        self.train_data_service.obtain_data_for_train.return_value = \
            TrainData(make_raw_train_data(seats=10))

        self.booking_reference_service = Mock(IObtainBookingReferences)
        self.booking_reference_service.obtain_booking_reference.return_value =\
            TEST_BOOKING_REFERENCE

        self.ticket_office = TicketOffice(self.train_data_service,
                                          self.booking_reference_service)

    def test_reserve_one_seat_in_empty_coach(self):
        self.assertEqual(build_reservation(nb_seats=1),
                         self.ticket_office.reserve(TRAIN_ID, 1))

    def test_reserve_two_seats_in_empty_coach(self):
        self.assertEqual(build_reservation(nb_seats=2),
                         self.ticket_office.reserve(TRAIN_ID, 2))

    def test_reserve_one_seat_in_almost_full_coach(self):
        self.train_data_service.obtain_data_for_train.return_value = \
            TrainData(make_raw_train_data(seats=10,
                                          reserved_seats=7,
                                          booking_reference=TEST_BOOKING_REFERENCE))

        self.assertEqual(build_empty_reservation(),
                         self.ticket_office.reserve(TRAIN_ID, 1))

    def test_booking_reference_is_fetched(self):
        other_booking_reference = 'dabbad00'
        self.booking_reference_service.obtain_booking_reference.return_value =\
            other_booking_reference

        self.assertEqual(other_booking_reference,
                         self.ticket_office.reserve(TRAIN_ID, 1)['booking_reference'])


def build_empty_reservation():
    return {
        'train_id': TRAIN_ID,
        'booking_reference': NO_BOOKING_REFERENCE,
        'seats': []
    }


def build_reservation(nb_seats):
    if 0 == nb_seats:
        return build_empty_reservation()

    return {
        'train_id': TRAIN_ID,
        'booking_reference': TEST_BOOKING_REFERENCE,
        'seats': ['{0}A'.format(x) for x in range(1, nb_seats + 1)]
    }
