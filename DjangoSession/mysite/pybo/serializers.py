#product/serializers.py
from rest_framework import serializers
from .models import Question

class QuestionSerializer(serializers.ModelSerializer) :
    class Meta :
        model = Question        # product 모델 사용
        fields = '__all__'            # 모든 필드 포함
