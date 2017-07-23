from abc import ABC, abstractmethod

NO_BOOKING_REFERENCE = ''


class TrainDataService(ABC):
    @abstractmethod
    def get_data_for_train(self, train_id):
        pass
