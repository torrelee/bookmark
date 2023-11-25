from django.urls import path
from .views import *

urlpatterns = [
    # 함수형 뷰는 이름만 써줘도 되지만 클래스형 뷰는 뒤에 반드시 .as_view()를 붙여야 한다.
    # 마지막 인자인 name은 설정한 이름을 가지고 해당 URL 패턴을 찾는 역할을 한다.
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    # <int:pk>의 int는 타입(컨버터) 기능이며 클래스 형태이다. pk는 컨버터를 통해 반환받은 값 혹은 패턴에 일치하는 값의 변수명이다.
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete')
]