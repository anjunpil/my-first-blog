from django.db import models
from django.conf import settings
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
		
#Post - model name
#models.CharField -글자수 제한된 텍스트 정의할때
#models.TextField -글자수 제한이 없는 긴 텍스트 속성
#models.DateTimeField -날짜와 시간을 의미
#models.Foreignkey - 다른 모델에 대한 링크
#__str__ (Post)제목 텍스트를 얻음

		