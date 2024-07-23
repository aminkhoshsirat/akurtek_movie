from django.db import models
from django.shortcuts import reverse
from django_jalali.db import models as jmodels
from apps.user.models import UserModel
from ckeditor.fields import RichTextField


class BlogCategoryModel(models.Model):
    title = models.CharField(max_length=1000)
    image = models.ImageField(upload_to='blog/category_image')
    url = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('blog:category', args=[self.url])


class BlogKeyWordModel(models.Model):
    title = models.CharField(max_length=1000)
    url = models.SlugField(unique=True, allow_unicode=True)

    def get_absolute_url(self):
        return reverse('blog:tag', args=[self.url])


class AutherModel(UserModel):
    name = models.CharField(max_length=500)
    url = models.SlugField(unique=True, allow_unicode=True)
    description = models.TextField()
    telegram_link = models.URLField()
    instagram_link = models.URLField()
    twitter_link = models.URLField()

    def get_absolute_url(self):
        return reverse('blog:auther', args=[self.url])


class BlogModel(models.Model):
    auther = models.ManyToManyField(AutherModel, related_name='auther_blogs')
    title = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='blog/image')
    description = models.TextField()
    category = models.ForeignKey(BlogCategoryModel, on_delete=models.DO_NOTHING, related_name='category_blogs')
    url = models.SlugField(unique=True, allow_unicode=True)
    published_date = jmodels.jDateTimeField(auto_now_add=True)
    update_date = jmodels.jDateTimeField(auto_now=True)
    read_time = models.CharField(max_length=250)
    conclusion = models.TextField()
    text = RichTextField()
    grade = models.PositiveIntegerField()
    keyword = models.ManyToManyField(BlogKeyWordModel, related_name='blog_keywords')
    active = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse('blog:blog_detail', args=[self.url])


class BlogLikeModel(models.Model):
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='blog_likes')
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user_blog_likes')
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)


class BlogCommentModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user_blog_comments')
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='blog_comments')
    text = models.TextField()
    parent = models.ForeignKey('BlogCommentModel', on_delete=models.CASCADE, related_name='comment_child', null=True, blank=True)
    published_date = jmodels.jDateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    admin_seen = models.BooleanField(default=True)


class BlogViewModel(models.Model):
    ip = models.CharField(max_length=100)
    user = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING, related_name='user_blog_view', null=True, blank=True)
    blog = models.ForeignKey(BlogModel, on_delete=models.CASCADE, related_name='blog_view')
    date_view = jmodels.jDateTimeField(auto_now_add=True)




