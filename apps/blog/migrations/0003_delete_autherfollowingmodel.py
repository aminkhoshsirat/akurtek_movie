# Generated by Django 4.1 on 2024-07-11 16:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogmodel_grade_remove_blogmodel_category_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='AutherFollowingModel',
        ),
    ]
