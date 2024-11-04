from account.entity.profile import Profile
from account.repository.profile_repository import ProfileRepository


class ProfileRepositoryImpl(ProfileRepository):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()

        return cls.__instance

    def create(self, email, user_name, account):
        profile = Profile.objects.create(email=email, user_name=user_name, account=account)
        return profile

    def findByEmail(self, email):
        try:
            return Profile.objects.get(email=email)
        except Profile.DoesNotExist:
            return None
        except Exception as e:
            print("이메일로 프로필 찾는 중 에러 발생:", e)
            raise e

    def findByUserName(self, user_name):
        try:
            return Profile.objects.get(user_name=user_name)
        except Profile.DoesNotExist:
            return None
        except Exception as e:
            print("유저 이름으로 프로필 찾는 중 에러 발생:", e)
            raise e

