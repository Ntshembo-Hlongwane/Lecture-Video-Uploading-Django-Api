from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser, JSONParser
from .models import LectureVideos
from .serializers import LectureVideoSerialzer




@api_view(['GET'])
def apiOverview(request):

    api_urls = {

        'Lecture-Videos' : 'videos-list/',
        'Upload-lecture-video': 'video-upload/',
        'Delete-lecture-video' : 'delete-lecture/'
    }

    return Response(api_urls)



@api_view(['GET'])
def getLectureVideos(request):

    videos = LectureVideos.objects.all()
    serializer = LectureVideoSerialzer(videos, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def uploadLectureVideo(request):

    parser_classes = (JSONParser, FormParser, MultiPartParser)
    serializer = LectureVideoSerialzer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    else:
        print('Errors: ' + str(serializer.data))

    return Response(serializer.data)

