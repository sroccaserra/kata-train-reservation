from unittest import TestCase

from domain.ticket_office import TicketOffice


class TrainsWithOneCoach(TestCase):
    def test_reserve_one_seat_in_empty_coach(self):
        ticket_office = TicketOffice()
        expected_reservation =\
            '{"train_id": "express_2000", "booking_reference": "75bcd15", "seats": ["1A"]}'

        self.assertEqual(expected_reservation,
                         ticket_office.reserve('express_2000', 1))
