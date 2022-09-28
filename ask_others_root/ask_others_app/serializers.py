from rest_framework import serializers, status
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password

from .models import User, Question, Survey, SurveyResponse, Response, ResponseType, ResponseVariant


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'avatar_link', 'password', 'created_at', 'updated_at']
        extra_kwargs = {'password': {'write_only': True}}


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

    class Meta:
        model = User
        fields = ('email', 'username', 'password')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class SurveyResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyResponse
        fields = '__all__'


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Response
        fields = '__all__'


class ResponseTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseType
        fields = '__all__'


class ResponseVariantSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseVariant
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    response_variants = ResponseVariantSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Survey
        fields = '__all__'
