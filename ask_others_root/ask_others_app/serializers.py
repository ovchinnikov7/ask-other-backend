from rest_framework import serializers, status
from rest_framework.fields import empty
from .models import User, Question, Survey, CompletedSurvey


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'avatarLink', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

    def validate_empty_values(self, data):
        if isinstance(data, User) or data.get('is_from_google'):
            return True, data

        return super().validate_empty_values(data)

    def run_validation(self, data=empty):
        (is_empty_value, data) = self.validate_empty_values(data)
        if is_empty_value:
            return data
        value = self.to_internal_value(data)
        self.run_validators(value)
        return value


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = '__all__'


class CompletedSurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompletedSurvey
        fields = '__all__'
