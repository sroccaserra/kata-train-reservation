from unittest import TestCase
from unittest.mock import Mock

import requests
from pytest import mark

from infrastructure.service_providers.train_data_service import TrainDataService
from test.common import TRAIN_ID


class TestTrainDataService(TestCase):
    def test_building_train_info(self):
        # Given
        http_service = Mock(requests)
        http_service.get.return_value.json.return_value = build_train_data()
        train_data_service = TrainDataService(http_service)
        # When
        train_info = train_data_service.obtain_info_for_train(TRAIN_ID)
        # Then
        self.assertTrue(train_info.can_reserve_seats(1))
        self.assertFalse(train_info.can_reserve_seats(2))
        self.assertEqual(train_info.get_some_free_seat_ids(1), ['1A'])


@mark.integration
class TestRealTrainDataService(TestCase):
    def test_building_train_info(self):
        # Given
        train_data_service = TrainDataService(requests)
        # When
        train_info = train_data_service.obtain_info_for_train(TRAIN_ID)
        # Then
        self.assertTrue(train_info.can_reserve_seats(11))
        self.assertFalse(train_info.can_reserve_seats(12))


def build_train_data():
    return {
        'seats': {
            '1A': {
                'seat_number': '1',
                'coach': 'A',
                'booking_reference': ''
            },
            '2A': {
                'seat_number': '2',
                'coach': 'A',
                'booking_reference': ''
            }
        }
    }
