from ai_result.entity.backlogs import Backlog
from ai_result.entity.code_review import CodeReview
from ai_result.entity.file_content import FileContent
from ai_result.entity.file_list import FileList
from ai_result.entity.project import Project
from ai_result.entity.test_report import TestReport
from ai_result.repository.ai_result_repository import AIResultRepository


class AIResultRepositoryImpl(AIResultRepository):
    __instance = None

    @classmethod
    def getInstance(cls):
        if cls.__instance is None:
            cls.__instance = cls()
        return cls.__instance

    def get_project_list(self, account_id):
        projects = Project.objects.filter(account__id=account_id).values_list('project_name', flat=True)
        return {'project_list': projects}

        # 백로그 저장
    def save_backlogs(self, account_id, project_name, backlog_data):
        project, _ = Project.objects.get_or_create(account_id=account_id, project_name=project_name)
        Backlog.objects.filter(project_id=project.id).delete()  # 기존 백로그 삭제
        Backlog.objects.create(project=project, description=backlog_data)

    # 백로그 조회
    def get_backlogs(self, account_id, project_name):
        project = Project.objects.get(account_id=account_id, project_name=project_name)
        backlogs = Backlog.objects.filter(project=project)
        return {'project_name': project_name, 'backlogs': [backlog.description for backlog in backlogs]}

    # 파일 리스트 저장
    def save_file_list(self, account_id, project_name, file_list):
        project, _ = Project.objects.get_or_create(account_id=account_id, project_name=project_name)
        FileList.objects.filter(project_id=project.id).delete()  # 기존 파일 삭제
        FileList.objects.create(project=project, description=file_list)

    # 파일 콘텐츠 조회
    def get_file_list(self, account_id, project_name):
        project = Project.objects.get(account_id=account_id, project_name=project_name)
        files = FileList.objects.filter(project=project)
        return {'project_name': project_name, 'files': [file.description for file in files]}

    def save_file_content(self, account_id, project_name, file_name, file_content):
        project, _ = Project.objects.get_or_create(account_id=account_id, project_name=project_name)
        FileContent.objects.filter(project=project, file_name=file_name).delete()  # 기존 파일 삭제
        FileContent.objects.create(project=project, file_name=file_name, file_content=file_content)

    # 파일 콘텐츠 조회
    def get_file_content(self, account_id, project_name):
        project = Project.objects.get(account_id=account_id, project_name=project_name)
        files = FileContent.objects.filter(project=project)
        return {
            'project_name': project_name,
            'files': [{'file_name': file.file_name, 'file_content': file.file_content} for file in files]
        }

    # 코드 리뷰 저장
    def save_test_reports(self, account_id, project_name, test_reports):
        project, _ = Project.objects.get_or_create(account_id=account_id, project_name=project_name)
        TestReport.objects.filter(project_id=project.id).delete()  # 기존 리포트 삭제
        TestReport.objects.create(project=project, report_content=test_reports)

    # 코드 리뷰 조회
    def get_test_reports(self, account_id, project_name):
        project = Project.objects.get(account_id=account_id, project_name=project_name)
        test_reports = TestReport.objects.filter(project=project)
        return {'project_name': project_name, 'test_reports': [test_report.report_content for test_report in test_reports]}

    def save_code_review(self, account_id, project_name, code_review):
        project, _ = Project.objects.get_or_create(account_id=account_id, project_name=project_name)
        CodeReview.objects.filter(project_id=project.id).delete()  # 기존 리포트 삭제
        CodeReview.objects.create(project=project, code_review=code_review)

    # 테스트 리포트 조회
    def get_code_review(self, account_id, project_name):
        project = Project.objects.get(account_id=account_id, project_name=project_name)
        code_review = CodeReview.objects.filter(project=project)
        return {'project_name': project_name, 'code_review': [code_review.code_review for code_review in code_review]}

