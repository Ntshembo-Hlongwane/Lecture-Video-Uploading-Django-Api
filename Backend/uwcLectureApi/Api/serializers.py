from  rest_framework import serializers
from .models import LectureVideos


class LectureVideoSerialzer(serializers.ModelSerializer):

    class Meta:
        model = LectureVideos
        fields = '__all__'


        