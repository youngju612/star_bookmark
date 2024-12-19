from django.shortcuts import redirect, get_object_or_404, redirect
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse, reverse_lazy

from .models import Bookmark

# Create your views here.
class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6
    template_name = 'bookmark/bookmark_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        favorite = self.request.GET.get('favorite')  # URL 쿼리 파라미터로 즐겨찾기 필터링
        if favorite == 'True':
            queryset = queryset.filter(favorite=True)  # 즐겨찾기만 필터링
        return queryset

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark
    template_name = 'bookmark/bookmark_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['favorite'] = self.object.favorite
        return context

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

# 즐겨찾기 상태 변경 뷰 추가
def toggle_favorite(request, pk):
    bookmark = get_object_or_404(Bookmark, pk=pk)
    bookmark.favorite = not bookmark.favorite  # 현재 상태를 반전
    bookmark.save()
    return redirect(reverse('list'))  # 북마크 리스트로 리디렉션
