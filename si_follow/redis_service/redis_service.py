from abc import ABC, abstractmethod


class RedisService(ABC):
    @abstractmethod
    def store_access_token(self, account_id, userToken, accessToken):
        pass
    @abstractmethod
    def get_value_by_key(self, key):
        pass

    @abstractmethod
    def delete_key(self, key):
        pass

    @abstractmethod
    def generate_and_store_access_token(self, profileRepository, email, accessToken):
        pass

    @abstractmethod
    def delete_access_token(self, userToken):
        pass