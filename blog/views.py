from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView,
)


from blog.models import Blog


class BlogCreateView(CreateView):
    model = Blog
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:article_list")


class BlogListView(ListView):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    model = Blog
    fields = ("title", "content", "preview")
    success_url = reverse_lazy("blog:article_list")


class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy("blog:article_list")
