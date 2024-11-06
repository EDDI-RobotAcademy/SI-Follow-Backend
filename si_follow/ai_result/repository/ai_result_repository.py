from abc import ABC, abstractmethod

class AIResultRepository(ABC):

    @abstractmethod
    def get_project_list(self, account_id):
        pass

    @abstractmethod
    def save_backlogs(self, account_id, project_name, backlog_data):
        pass

    @abstractmethod
    def get_backlogs(self, account_id, project_name):
        pass

    @abstractmethod
    def save_file_list(self, account_id, project_name, file_list):
        pass

    @abstractmethod
    def get_file_list(self, account_id, project_name):
        pass

    @abstractmethod
    def save_file_content(self, account_id, project_name, file_name, file_content):
        pass

    @abstractmethod
    def get_file_content(self, account_id, project_name):
        pass

    @abstractmethod
    def save_test_reports(self, account_id, project_name, test_reports):
        pass

    @abstractmethod
    def get_test_reports(self, account_id, project_name):
        pass

    @abstractmethod
    def save_code_review(self, account_id, project_name, code_review):
        pass

    @abstractmethod
    def get_code_review(self, account_id, project_name):
        pass

