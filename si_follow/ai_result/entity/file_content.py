from django.db import models

from ai_result.entity.project import Project


class FileContent(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    file_name = models.CharField(max_length=255)
    file_content = models.TextField()

    def __str__(self):
        return f"FileContent -> (Project: {self.project.project_name})"
