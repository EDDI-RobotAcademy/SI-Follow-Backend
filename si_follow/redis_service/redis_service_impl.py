import uuid
import redis
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from redis_service.redis_service import RedisService


class RedisServiceImpl(RedisService):
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self):
        if not hasattr(self, 'redis_client'):  # 이미 초기화된 경우 중복 방지
            self.redis_client = redis.Redis(
                host=settings.REDIS_HOST,
                port=settings.REDIS_PORT,
                password=settings.REDIS_PASSWORD,
                decode_responses=True
            )

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    # accessToken과 account_id를 Redis에 저장
    def store_access_token(self, account_id, userToken, accessToken, ttl=3600 * 24):
        try:
            # print(f"Storing token for userToken: {userToken} with TTL: {ttl}")
            # Redis 해시로 저장
            self.redis_client.hset(userToken, mapping={
                'account_id': account_id,
                'access_token': accessToken
            })

            # TTL 설정
            success = self.redis_client.expire(userToken, ttl)
            # print(f"TTL set success: {success}")

        except Exception as e:
            print(f"Error storing access token in Redis: {e}")

    # Redis에서 userToken으로 account_id와 accessToken 조회
    def get_value_by_key(self, userToken):
        try:
            return self.redis_client.hgetall(userToken)  # 모든 필드(account_id, access_token) 조회
        except Exception as e:
            print(f"Error retrieving token from Redis: {e}")
            raise e

    def get_value_by_access_token(self, accessToken):
        try:
            for key in self.redis_client.scan_iter():
                if self.redis_client.type(key) != 'hash':
                    continue  # 해시가 아닌 키는 무시
                data = self.redis_client.hgetall(key)
                if data.get('access_token') == accessToken:
                    return {'userToken': key, 'account_id': data.get('account_id'), 'access_token': accessToken}
            return None
        except Exception as e:
            print(f"Error retrieving account by access token from Redis: {e}")
            raise e

    def delete_key(self, key):
        try:
            result = self.redis_client.delete(key)
            if result == 1:
                print(f"Successfully deleted token: {key}")
                return True
            return False
        except Exception as e:
            print(f"Error deleting token from Redis: {e}")
            raise e

    # 분리된 redisAccessToken 로직: accessToken을 포함하여 저장
    def generate_and_store_access_token(self, profileRepository, user_name, accessToken, ttl=3600 * 24):
        try:
            account = profileRepository.findByUserName(user_name)
            if not account:
                return Response({'error': 'Account not found'}, status=status.HTTP_404_NOT_FOUND)

            userToken = str(uuid.uuid4())
            print(f"Generated token for account: {account.id}")

            # account_id와 accessToken을 저장하고 TTL 설정
            self.store_access_token(account.id, userToken, accessToken, ttl)

            # 추가: TTL이 적용된 키가 Redis에 있는지 확인
            stored_data = self.get_value_by_key(userToken)
            if not stored_data:
                print(f"Error: userToken {userToken} not found in Redis after storage.")
                return Response({'error': 'Failed to store token in Redis'},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            return Response({'userToken': userToken}, status=status.HTTP_200_OK)

        except Exception as e:
            print(f"Error storing access token in Redis: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    # 분리된 dropRedisTokenForLogout 로직: userToken을 사용해 Redis에서 키 삭제
    def delete_access_token(self, userToken):
        try:
            isSuccess = self.delete_key(userToken)
            return Response({'isSuccess': isSuccess}, status=status.HTTP_200_OK)
        except Exception as e:
            print(f"Error deleting token from Redis: {str(e)}")
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
