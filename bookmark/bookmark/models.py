from django.db import models
from django.urls import reverse

class Bookmark(models.Model):
    # 두 개의 클래스 변수(필드)를 만든다.
    # 이 정보들이 기록되는 테이블 이름은 bookmark 이다.
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    def __str__(self):
        # 객체를 출력할 때 나타날 값(항상 반환값은 문자열이어야 한다)
        return "이름 : " + self.site_name + ", 주소 : " + self.url
    def get_absolute_url(self):
        # reverse 메서드는 URL 패턴의 이름과 추가 인자를 전달받아 URL을 생성한다.
        return reverse('detail', args=[str(self.id)])
