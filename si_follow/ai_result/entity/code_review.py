from django.db import models

from ai_result.entity.project import Project


class CodeReview(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    code_review = models.TextField()

    def __str__(self):
        return f"CodeReview -> (Project: {self.project.project_name})"
