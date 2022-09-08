from rest_framework import routers
from django.urls import path, include

from .views import (UserViewSet, QuestionViewSet, SurveyViewSet,
                    SurveyResponseViewSet, ResponseViewSet,
                    ResponseTypeViewSet, ResponseVariantViewSet)

router = routers.SimpleRouter(trailing_slash=True)
router.register(r'users', UserViewSet)
router.register(r'questions', QuestionViewSet)
router.register(r'surveys', SurveyViewSet)
router.register(r'survey_responses', SurveyResponseViewSet)
router.register(r'responses', ResponseViewSet)
router.register(r'response_types', ResponseTypeViewSet)
router.register(r'response_variants', ResponseVariantViewSet)

urlpatterns = [
    *router.urls,
]
