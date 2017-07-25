from domain.i_obtain_train_info import IObtainTrainInfo
from domain.train_info import TrainInfo, TrainId


class TrainDataService(IObtainTrainInfo):
    def __init__(self, http_service):
        self._http_service = http_service
        self._base_url = 'http://localhost:8081/data_for_train/'

    def obtain_info_for_train(self, train_id: TrainId) -> TrainInfo:
        response = self._http_service.get(self._base_url + train_id)
        raw_data = response.json()
        return build_train_info(raw_data)


def build_train_info(raw_data) -> TrainInfo:
    seats_data = raw_data['seats'].values()
    return TrainInfo(seats_data)
