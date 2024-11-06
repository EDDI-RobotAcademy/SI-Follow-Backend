from account.repository.profile_repository_impl import ProfileRepositoryImpl
from ai_result.repository.ai_result_repository_impl import AIResultRepositoryImpl
from ai_result.service.ai_result_service import AIResultService
from redis_service.redis_service_impl import RedisServiceImpl
import requests

from si_follow import settings


class AIResultServiceImpl(AIResultService):
    def __init__(self):
        self.ai_result_repository = AIResultRepositoryImpl()
        self.redis_service = RedisServiceImpl.getInstance()
        self.fast_api_url = settings.FAST_API_URL
        self.profile_repository = ProfileRepositoryImpl.getInstance()

    def get_project_list(self, user_token):
        stored_data = self.redis_service.get_value_by_key(user_token)
        if 'account_id' not in stored_data:
            return {'error': '유효하지 않은 user_token'}
        account_id = stored_data['account_id']
        return self.ai_result_repository.get_project_list(account_id)

    # 백로그 저장
    def store_backlogs(self, user_name, project_name, backlog_data):
        # 데이터베이스에서 user_name으로 account_id 조회
        profile = self.profile_repository.findByUserName(user_name)
        if not profile:
            return {'error': '유효하지 않은 user_name'}

        account_id = profile.account.id
        self.ai_result_repository.save_backlogs(account_id, project_name, backlog_data)
        return {'message': '백로그 저장 완료'}

    # 백로그 조회
    def get_backlogs(self, user_token, project_name):
        stored_data = self.redis_service.get_value_by_key(user_token)
        if 'account_id' not in stored_data:
            return {'error': '유효하지 않은 user_token'}

        account_id = stored_data['account_id']
        return self.ai_result_repository.get_backlogs(account_id, project_name)

    # 파일 리스트 저장
    def store_file_list(self, user_name, project_name, file_list):
        profile = self.profile_repository.findByUserName(user_name)
        if not profile:
            return {'error': '유효하지 않은 user_name'}

        account_id = profile.account.id
        self.ai_result_repository.save_file_list(account_id, project_name, file_list)
        return {'message': '파일 리스트 저장 완료'}

    # 파일 리스트 조회

    def get_file_list(self, user_token, project_name):
        stored_data = self.redis_service.get_value_by_key(user_token)
        if 'account_id' not in stored_data:
            return {'error': '유효하지 않은 user_token'}

        account_id = stored_data['account_id']
        return self.ai_result_repository.get_file_list(account_id, project_name)

    # 파일 내용 저장
    def store_file_content(self, user_name, project_name, file_name, file_content):
        profile = self.profile_repository.findByUserName(user_name)
        if not profile:
            return {'error': '유효하지 않은 user_name'}

        account_id = profile.account.id
        self.ai_result_repository.save_file_content(account_id, project_name, file_name, file_content)
        return {'message': '파일 내용 저장 완료'}

    # 파일 리스트 조회
    def get_file_content(self, user_token, project_name):
        stored_data = self.redis_service.get_value_by_key(user_token)
        if 'account_id' not in stored_data:
            return {'error': '유효하지 않은 user_token'}

        account_id = stored_data['account_id']
        return self.ai_result_repository.get_file_content(account_id, project_name)

    # 테스트 리포트 저장
    def store_test_reports(self, user_name, project_name, test_reports):
        profile = self.profile_repository.findByUserName(user_name)
        if not profile:
            return {'error': '유효하지 않은 user_name'}

        account_id = profile.account.id
        self.ai_result_repository.save_test_reports(account_id, project_name, test_reports)
        return {'message': '테스트 리포트 저장 완료'}

    # 테스트 리포트 조회
    def get_test_reports(self, user_token, project_name):
        stored_data = self.redis_service.get_value_by_key(user_token)
        if 'account_id' not in stored_data:
            return {'error': '유효하지 않은 user_token'}

        account_id = stored_data['account_id']
        return self.ai_result_repository.get_test_reports(account_id, project_name)

    # 코드 리뷰 저장
    def store_code_review(self, user_name, project_name, code_review):
        profile = self.profile_repository.findByUserName(user_name)
        if not profile:
            return {'error': '유효하지 않은 user_name'}

        account_id = profile.account.id
        self.ai_result_repository.save_code_review(account_id, project_name, code_review)
        return {'message': '코드 리뷰 저장 완료'}

    # 코드 리뷰 조회
    def get_code_review(self, user_token, project_name):
        stored_data = self.redis_service.get_value_by_key(user_token)
        if 'account_id' not in stored_data:
            return {'error': '유효하지 않은 user_token'}

        account_id = stored_data['account_id']
        return self.ai_result_repository.get_code_review(account_id, project_name)
