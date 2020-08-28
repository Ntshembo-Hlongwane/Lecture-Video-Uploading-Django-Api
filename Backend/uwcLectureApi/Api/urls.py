from django.urls import path
from .views import apiOverview, getLectureVideos, uploadLectureVideo

urlpatterns = [
    
    path('', apiOverview, name='ApiOverView'),
    path('videos-list/', getLectureVideos, name='lecture-video-list'),
    path('video-upload/', uploadLectureVideo, name='lecture-video-upload'),
]
