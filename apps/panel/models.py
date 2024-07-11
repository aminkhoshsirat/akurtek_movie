from django.db import models
from apps.movie.models import MovieModel, SeriesModel


class SiteDetailModel(models.Model):
    logo = models.ImageField(upload_to='site_detail/logo')
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    blog_background = models.ImageField(upload_to='site_detail/background')
    privacy_background = models.ImageField(upload_to='site_detail/background')
    faq_background = models.ImageField(upload_to='site_detail/background')
    about_us_background = models.ImageField(upload_to='site_detail/background')
    default_user_profile = models.ImageField(upload_to='site_detail/profile')


class BannerModel(models.Model):
    movie = models.OneToOneField(MovieModel, on_delete=models.CASCADE, null=True, blank=True)
    series = models.OneToOneField(SeriesModel, on_delete=models.CASCADE, null=True, blank=True)
    active = models.BooleanField(default=True)


class PrivacyModel(models.Model):
    title = models.CharField(max_length=10000)
    description = models.TextField()
    order = models.PositiveIntegerField(unique=True)


class PopularQuestionsModel(models.Model):
    title = models.CharField(max_length=10000)
    description = models.TextField()
    order = models.PositiveIntegerField(unique=True)


class ContactUsModel(models.Model):
    name = models.CharField(max_length=1000)
    family_name = models.CharField(max_length=1000)
    phone = models.CharField(max_length=11)
    email = models.EmailField()
    message = models.TextField()
    seen_by_admin = models.BooleanField(default=False)
    admin_message = models.TextField(null=True, blank=True)