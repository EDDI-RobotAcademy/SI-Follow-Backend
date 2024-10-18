from abc import ABC, abstractmethod


class AIResultService(ABC):

    @abstractmethod
    def fetch_and_store_backlogs(self, user_token, project_name):
        pass

    @abstractmethod
    def get_backlogs(self, user_token, project_name):
        pass
