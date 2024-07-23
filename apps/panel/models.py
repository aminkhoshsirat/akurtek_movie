from django.db import models
from apps.movie.models import MovieModel, SeriesModel
from apps.user.models import UserModel


class SiteDetailModel(models.Model):
    logo = models.ImageField(upload_to='site_detail/logo')
    user_non_profile_image = models.ImageField(upload_to='site_detail/image')
    title = models.CharField(max_length=10000)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    blog_background = models.ImageField(upload_to='site_detail/background')
    privacy_background = models.ImageField(upload_to='site_detail/background')
    faq_background = models.ImageField(upload_to='site_detail/background')
    about_us_background = models.ImageField(upload_to='site_detail/background')
    pricing_plan_background = models.ImageField(upload_to='site_detail/background')
    buy_plan_background = models.ImageField(upload_to='site_detail/background')
    about_us_image = models.ImageField(upload_to='site_detail/background')
    twitter = models.URLField(null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    telegram = models.URLField(null=True, blank=True)
    whatsup = models.URLField(null=True, blank=True)
    google_plus = models.URLField(null=True, blank=True)
    github = models.URLField(null=True, blank=True)
    application_google_play_image = models.ImageField(upload_to='site_detail/application', null=True, blank=True)
    application_ios_image = models.ImageField(upload_to='site_detail/application', null=True, blank=True)
    application_google_play_url = models.URLField(null=True, blank=True)
    application_ios_url = models.URLField(null=True, blank=True)
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


class TeamPositionModel(models.Model):
    title = models.CharField(max_length=10000)

    def __str__(self):
        return self.title


class TeamMembersModel(UserModel):
    position = models.ForeignKey(TeamPositionModel, on_delete=models.DO_NOTHING, related_name='positions_members')
    description = models.TextField()
    telegram_link = models.URLField()
    instagram_link = models.URLField()
    twitter_link = models.URLField()


class PricingPlanModel(models.Model):
    title = models.CharField(max_length=10000)
    period = models.PositiveIntegerField()
    price = models.PositiveIntegerField()
    active = models.BooleanField(default=True)
