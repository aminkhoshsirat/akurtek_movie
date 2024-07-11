from django.db import models


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
    video = models.FileField(upload_to='movie/video')
    description = models.TextField()
    time = models.TimeField()
    actors = models.ManyToManyField(ActorModel, related_name='actor_movies')
    grade = models.FloatField()
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.title


class SeriesModel(models.Model):
    title = models.CharField(max_length=10000)
    category = models.ManyToManyField(CategoryModel, related_name='category_series')
    actors = models.ManyToManyField(ActorModel, related_name='actor_serials')
    grade = models.FloatField()

    def __str__(self):
        return self.title


class SeriesSeasonModel(models.Model):
    series = models.ForeignKey(SeriesModel, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=10000)
    description = models.TextField()


class SerialPartModel(models.Model):
    season = models.ForeignKey(SeriesSeasonModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=10000)
    video = models.FileField(upload_to='serial/video')
    description = models.TextField()
    tags = models.ManyToManyField(TagModel, related_name='tag_serials')
    image = models.ImageField(upload_to='serial/image')
    trailer = models.FileField(upload_to='serial/trailer')
    time = models.PositiveIntegerField()

    def __str__(self):
        return self.title
