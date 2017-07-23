from unittest import TestCase

from domain.ticket_office import TicketOffice


class TrainsWithOneCoach(TestCase):
    def build_reservation(self, nb_seats):
        reservation_with_one_seat = {
            'train_id': 'express_2000',
            'booking_reference': '75bcd15',
            'seats': ['{0}A'.format(x) for x in range(1, nb_seats + 1)]
        }
        return reservation_with_one_seat

    def setUp(self):
        self.ticket_office = TicketOffice()

    def test_reserve_one_seat_in_empty_coach(self):
        self.assertEqual(self.build_reservation(1),
                         self.ticket_office.reserve('express_2000', 1))

    def test_reserve_two_seats_in_empty_coach(self):
        self.assertEqual(self.build_reservation(2),
                         self.ticket_office.reserve('express_2000', 2))
