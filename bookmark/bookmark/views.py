from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark

class BookmarkListView(ListView):
    # Model 설정
    model = Bookmark
    paginate_by = 6 # 한페이지에 몇 개씩 출력하는지 결정하는 값

class BookmarkCreateView(CreateView):
    # 어떤 모델의 입력을 받을 것인가?
    model = Bookmark
    # 어떤 필드들을 입력 받을 것인가?
    fields = ['site_name', 'url']
    # 글쓰기를 완료하고 이동할 페이지
    success_url = reverse_lazy('list')
    # 사용할 템플릿의 접미사만 변경하는 설정값(템플릿의 기본 이름은: 모델명_xxx)
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView): # 제네릭 뷰인 DetailView를 상속받는다.
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update' # 템플릿 접미사 때문에 bookmark_update.html이 템플릿이 된다.

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
