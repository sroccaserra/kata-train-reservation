from abc import ABC, abstractmethod

from domain.train_info import TrainInfo


class IObtainTrainInfo(ABC):
    @abstractmethod
    def obtain_info_for_train(self, train_id) -> TrainInfo:
        pass
