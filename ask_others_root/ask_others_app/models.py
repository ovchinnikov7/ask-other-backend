from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    avatar_link = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']
    objects = UserManager()

    def __str__(self):
        return self.email


class Survey(models.Model):
    author = models.ForeignKey(User, related_name='surveys', on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title


class ResponseType(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Question(models.Model):
    survey = models.ForeignKey(Survey, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    response_type = models.ForeignKey(ResponseType, on_delete=models.CASCADE)
    attachment = models.FileField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.text


class ResponseVariant(models.Model):
    question = models.ForeignKey(Question, related_name='response_variants', on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.text


class SurveyResponse(models.Model):
    survey = models.ForeignKey(Survey, related_name='survey_responses', on_delete=models.CASCADE)
    respondent = models.ForeignKey(User, related_name='survey_responses', on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)


class Response(models.Model):
    question = models.ForeignKey(Question, related_name='responses', on_delete=models.CASCADE)
    respondent = models.ForeignKey(SurveyResponse, related_name='responses', on_delete=models.CASCADE)
    variant_answer = models.ForeignKey(ResponseVariant, related_name='responses', on_delete=models.CASCADE)
    text_answer = models.TextField()
    created_at = models.DateTimeField(null=True, blank=True)
    updated_at = models.DateTimeField(null=True, blank=True)
