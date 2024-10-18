from ai_result.entity.backlogs import Backlog
from ai_result.entity.file_list import FileList
from ai_result.entity.project import Project
from ai_result.entity.test_report import TestReport
from ai_result.repository.ai_result_repository import AIResultRepository


class AIResultRepositoryImpl(AIResultRepository):

    # 백로그 저장
    def save_backlogs(self, account_id, project_name, backlog_data):
        project, _ = Project.objects.get_or_create(account_id=account_id, project_name=project_name)
        Backlog.objects.filter(project=project).delete()  # 기존 백로그 삭제
        Backlog.objects.create(project=project, description=backlog_data)

    # 백로그 조회
    def get_backlogs(self, account_id, project_name):
        project = Project.objects.get(account_id=account_id, project_name=project_name)
        backlogs = Backlog.objects.filter(project=project)
        return {'project_name': project_name, 'backlogs': [backlog.description for backlog in backlogs]}


