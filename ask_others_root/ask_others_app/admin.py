from django.contrib import admin

from .models import User, Question, Survey, SurveyResponse, Response, ResponseType, ResponseVariant

admin.site.register(User)
admin.site.register(Question)
admin.site.register(Survey)
admin.site.register(SurveyResponse)
admin.site.register(Response)
admin.site.register(ResponseType)
admin.site.register(ResponseVariant)
