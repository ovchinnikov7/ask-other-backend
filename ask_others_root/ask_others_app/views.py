from rest_framework import filters, status, viewsets, authentication, permissions, response
from rest_framework.generics import CreateAPIView
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import MultiPartParser

from .models import User, Question, Survey, SurveyResponse, Response, ResponseType, ResponseVariant
from .serializers import (UserSerializer, RegisterSerializer, QuestionSerializer, SurveySerializer,
                          SurveyResponseSerializer, ResponseSerializer,
                          ResponseTypeSerializer, ResponseVariantSerializer)


class RegisterView(CreateAPIView):
    """Registers new user with provided credentials."""
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class ProfileView(APIView):
    """Gets user's profile data."""
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        user = UserSerializer(request.user).data
        return response.Response({
            "id": user["id"],
            "email": user["email"],
            "username": user["username"],
            "avatar": user["avatar_link"],
        })


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = (MultiPartParser,)


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class SurveyResponseViewSet(viewsets.ModelViewSet):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer


class ResponseViewSet(viewsets.ModelViewSet):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer


class ResponseTypeViewSet(viewsets.ModelViewSet):
    queryset = ResponseType.objects.all()
    serializer_class = ResponseTypeSerializer


class ResponseVariantViewSet(viewsets.ModelViewSet):
    queryset = ResponseVariant.objects.all()
    serializer_class = ResponseVariantSerializer
