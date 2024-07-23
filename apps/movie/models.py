from django.db import models
from django.urls import reverse


class CategoryModel(models.Model):
    title = models.CharField(max_length=10000)
    url = models.SlugField(allow_unicode=True)
    image = models.ImageField(upload_to='category/image')
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        pass


class TagModel(models.Model):
    title = models.CharField(max_length=10000)
    url = models.SlugField(allow_unicode=True)

    def __str__(self):
        return self.title


class ActorModel(models.Model):
    name = models.CharField(max_length=10000)
    url = models.SlugField(allow_unicode=True)

    def __str__(self):
        return self.name


class MovieModel(models.Model):
    title = models.CharField(max_length=10000)
    url = models.SlugField(allow_unicode=True)
    category = models.ManyToManyField(CategoryModel, related_name='category_movies')
    tags = models.ManyToManyField(TagModel, related_name='tag_movies')
    image = models.ImageField(upload_to='movie/image')
    trailer = models.FileField(upload_to='movie/trailer')
    description = models.TextField()
    time = models.TimeField()
    actors = models.ManyToManyField(ActorModel, related_name='actor_movies')
    grade = models.FloatField()
    sell_num = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie:movie_base', args=[self.url])


class SeriesModel(models.Model):
    title = models.CharField(max_length=10000)
    url = models.SlugField(allow_unicode=True)
    category = models.ManyToManyField(CategoryModel, related_name='category_series')
    tags = models.ManyToManyField(TagModel, related_name='tag_series')
    image = models.ImageField(upload_to='series/image')
    trailer = models.FileField(upload_to='series/trailer')
    description = models.TextField()
    actors = models.ManyToManyField(ActorModel, related_name='actor_series')
    grade = models.FloatField()
    age = models.PositiveIntegerField()
    sell_num = models.PositiveIntegerField()
    year = models.PositiveIntegerField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie:series_base', args=[self.url])


class MoviePartModel(models.Model):
    base = models.ForeignKey(MovieModel, on_delete=models.DO_NOTHING, related_name='movie_parts')
    title = models.CharField(max_length=10000)
    image = models.ImageField(upload_to='movie/image')
    url = models.SlugField()
    time = models.TimeField()
    trailer = models.FileField(upload_to='movie/trailer')
    video = models.FileField(upload_to='movie/video')
    description = models.TextField()
    like = models.PositiveIntegerField()
    product_year = models.PositiveIntegerField()
    age = models.PositiveIntegerField()
    year = models.PositiveIntegerField()

    def get_absolute_url(self):
        return reverse('movie:movie_detail', args=[self.url])


class SeriesSeasonModel(models.Model):
    series = models.ForeignKey(SeriesModel, on_delete=models.DO_NOTHING, related_name='series_season')
    title = models.CharField(max_length=10000)
    description = models.TextField()
    year = models.PositiveIntegerField()


class SeriesPartModel(models.Model):
    season = models.ForeignKey(SeriesSeasonModel, on_delete=models.CASCADE, related_name='season_parts')
    title = models.CharField(max_length=10000)
    url = models.SlugField(allow_unicode=True)
    video = models.FileField(upload_to='serial/video')
    description = models.TextField()
    tags = models.ManyToManyField(TagModel, related_name='tag_serials')
    image = models.ImageField(upload_to='serial/image')
    trailer = models.FileField(upload_to='serial/trailer')
    part_time = models.TimeField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('movie:series_detail', args=[self.url])
