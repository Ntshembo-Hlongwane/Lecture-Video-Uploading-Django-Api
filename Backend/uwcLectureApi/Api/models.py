from django.db import models


class LectureVideos(models.Model):

    lecturer = models.CharField(max_length=100, blank=False, null=False)
    module = models.CharField(max_length=100, blank=False, null=False)
    video = models.FileField(upload_to='lectures')
    date = models.CharField(max_length=100, blank=False, null=False)


    def __str__(self):
        return self.lecturer


    class Meta:
        verbose_name_plural = 'LectureVideos'
        
    