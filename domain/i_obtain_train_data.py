from abc import ABC, abstractmethod

NO_BOOKING_REFERENCE = ''


class IObtainTrainData(ABC):
    @abstractmethod
    def obtain_data_for_train(self, train_id):
        pass
