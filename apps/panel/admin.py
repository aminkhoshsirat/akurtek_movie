from django.contrib import admin
from .models import *


@admin.register(SiteDetailModel)
class SiteDetailAdmin(admin.ModelAdmin):
    list_display = ['title', 'phone', 'email']


@admin.register(BannerModel)
class BannerAdmin(admin.ModelAdmin):
    list_display = ['movie', 'series', 'active']


@admin.register(PrivacyModel)
class PrivacyAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']


@admin.register(PopularQuestionsModel)
class PopularQuestionAdmin(admin.ModelAdmin):
    list_display = ['title', 'order']


@admin.register(ContactUsModel)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['name', 'family_name', 'phone', 'email']


@admin.register(TeamPositionModel)
class TeamPositionAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(TeamMembersModel)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display = ['position', 'fullname']


@admin.register(PricingPlanModel)
class PricingPlanAdmin(admin.ModelAdmin):
    list_display = ['title', 'period', 'price', 'active']
