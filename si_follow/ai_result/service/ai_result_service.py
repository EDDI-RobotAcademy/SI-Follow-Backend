from abc import ABC, abstractmethod


class AIResultService(ABC):

    @abstractmethod
    def store_backlogs(self, user_token, project_name, backlog_data):
        pass

    @abstractmethod
    def get_backlogs(self, user_token, project_name):
        pass

    @abstractmethod
    def store_file_list(self, user_token, project_name,  file_list ):
        pass

    @abstractmethod
    def get_file_list(self, user_token, project_name):
        pass

    @abstractmethod
    def store_file_content(self, user_token, project_name,file_name, file_content):
        pass

    @abstractmethod
    def get_file_content(self, user_token, project_name):
        pass

    @abstractmethod
    def store_test_reports(self, user_token, project_name, test_reports):
        pass

    @abstractmethod
    def get_test_reports(self, user_token, project_name):
        pass

    @abstractmethod
    def store_code_review(self, user_token, project_name, code_review):
        pass

    @abstractmethod
    def get_code_review(self, user_token, project_name):
        pass