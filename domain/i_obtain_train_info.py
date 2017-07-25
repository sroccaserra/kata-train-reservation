from abc import ABC, abstractmethod

from domain.train_info import TrainInfo, TrainId


class IObtainTrainInfo(ABC):
    @abstractmethod
    def obtain_info_for_train(self, train_id: TrainId) -> TrainInfo:
        pass
