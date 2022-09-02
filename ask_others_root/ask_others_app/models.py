from django.db import models


class User(models.Model):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    avatarLink = models.TextField()

    def __str__(self):
        return self.username


class Survey(models.Model):
    authorId = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    createdAt = models.DateField()

    def __str__(self):
        return self.title


class Question(models.Model):
    surveyId = models.ForeignKey(User, related_name='survey', on_delete=models.CASCADE)
    text = models.TextField()
    responseType = models.IntegerField()
    attachment = models.FileField()

    def __str__(self):
        return self.text


class CompletedSurvey(models.Model):
    authorId = models.ForeignKey(User, related_name='author', on_delete=models.CASCADE)
    surveyId = models.ForeignKey(User, related_name='survey', on_delete=models.CASCADE)

    def __str__(self):
        return self.surveyId
