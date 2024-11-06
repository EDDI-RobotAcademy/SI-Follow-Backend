from rest_framework.response import Response
from rest_framework import status, viewsets

from ai_result.service.ai_result_service_impl import AIResultServiceImpl


class AIResultView(viewsets.ViewSet):
    ai_result_service = AIResultServiceImpl()

    def get_project_list(self, request):
        user_token= request.data.get('user_token')
        project_list = self.ai_result_service.get_project_list(user_token)
        return Response(project_list, status=status.HTTP_200_OK)

    # 백로그 저장 및 가져오기
    def store_backlogs(self, request):
        user_token = request.data.get('user_token')
        project_name = request.data.get('project_name')
        backlog_data = request.data.get('backlog')
        result = self.ai_result_service.store_backlogs(user_token, project_name, backlog_data)
        return Response(result, status=status.HTTP_200_OK)

    def get_backlogs(self, request):
        user_token = request.data.get('user_token')  # 기존 GET을 POST로 변경
        project_name = request.data.get('project_name')
        result = self.ai_result_service.get_backlogs(user_token, project_name)
        return Response(result, status=status.HTTP_200_OK)

    # 파일 리스트 저장 및 가져오기
    def store_file_list(self, request):
        user_token = request.data.get('user_token')
        project_name = request.data.get('project_name')
        file_list = request.data.get('file_list')
        result = self.ai_result_service.store_file_list(user_token, project_name, file_list)
        return Response(result, status=status.HTTP_200_OK)

    def get_file_list(self, request):
        user_token = request.data.get('user_token')
        project_name = request.data.get('project_name')
        result = self.ai_result_service.get_file_list(user_token, project_name)
        return Response(result, status=status.HTTP_200_OK)

    def store_file_content(self, request):
        user_token = request.data.get('user_token')
        project_name = request.data.get('project_name')
        file_name = request.data.get('file_name')
        file_content = request.data.get('file_content')
        result = self.ai_result_service.store_file_content(user_token, project_name, file_name, file_content)
        return Response(result, status=status.HTTP_200_OK)

    def get_file_content(self, request):
        user_token = request.data.get('user_token')
        project_name = request.data.get('project_name')
        result = self.ai_result_service.get_file_content(user_token, project_name)
        return Response(result, status=status.HTTP_200_OK)

    # 테스트 리포트 저장
    def store_test_reports(self, request):
        user_token = request.data.get('user_token')
        project_name = request.data.get('project_name')
        test_reports = request.data.get('test_reports')
        result = self.ai_result_service.store_test_reports(user_token, project_name, test_reports)
        return Response(result, status=status.HTTP_200_OK)

    def get_test_reports(self, request):
        user_token = request.data.get('user_token')
        project_name = request.data.get('project_name')
        result = self.ai_result_service.get_test_reports(user_token, project_name)
        return Response(result, status=status.HTTP_200_OK)

    def store_code_review(self, request):
        user_token = request.data.get('user_token')
        project_name = request.data.get('project_name')
        code_review = request.data.get('code_review')
        result = self.ai_result_service.store_code_review(user_token, project_name, code_review)
        return Response(result, status=status.HTTP_200_OK)

    def get_code_review(self, request):
        user_token = request.data.get('user_token')
        project_name = request.data.get('project_name')
        result = self.ai_result_service.get_code_review(user_token, project_name)
        return Response(result, status=status.HTTP_200_OK)