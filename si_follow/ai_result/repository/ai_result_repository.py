from abc import ABC, abstractmethod

class AIResultRepository(ABC):
    @abstractmethod
    def save_backlogs(self, account_id, project_name, backlog_data):
        pass

    @abstractmethod
    def get_backlogs(self, account_id, project_name):
        pass


