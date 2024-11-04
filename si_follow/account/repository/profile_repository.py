from abc import ABC, abstractmethod


class ProfileRepository(ABC):

    @abstractmethod
    def create(self, email, user_name, account):
        pass

    @abstractmethod
    def findByEmail(self, email):
        pass
