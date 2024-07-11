from django.shortcuts import render
from django.views import View
from django.contrib.postgres.search import TrigramSimilarity
from django.db.models.functions import Greatest
from django.views.generic import ListView, DetailView
from .models import *
from apps.panel.models import SiteDetailModel


class BlogView(ListView):
    template_name = 'blog/blog.html'
    model = BlogModel
    context_object_name = 'blogs'
    paginate_by = 20

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['top_blogs'] = BlogModel.objects.all().order_by('-grade')[0:20]
        context['categories'] = BlogCategoryModel.objects.filter(active=True)
        context['tags'] = BlogKeyWordModel.objects.all()
        context['site_detail'] = SiteDetailModel.objects.all().first()
        return context

    def get_queryset(self):
        search = self.request.GET.get('search')
        category = self.request.GET.get('category')
        tag = self.request.GET.get('tag')
        blogs = BlogModel.objects.filter(active=True)
        if category:
            blogs = blogs.filter(category__url=category)
        if tag:
            blogs = blogs.filter(tag__url=tag)
        if search:
            blogs = blogs.annotate(similar=Greatest(
                TrigramSimilarity('title', search),
                TrigramSimilarity('url', search),
                TrigramSimilarity('category__title', search),
            )).filter(similar__gt=0.1).order_by('-similar')

        return blogs


class BlogDetailView(DetailView):
    template_name = 'blog/blog-details.html'
    model = BlogModel
    queryset = BlogModel.objects.filter(active=True)
    context_object_name = 'blog'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['suggested_blogs'] = BlogModel.objects.filter(category=context['blog'].category)
        context['site_detail'] = SiteDetailModel.objects.all().first()
        context['categories'] = BlogCategoryModel.objects.filter(active=True)
        context['tags'] = BlogKeyWordModel.objects.all()
        return context

