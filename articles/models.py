from django.db import models

class Article(models.Model):
    title = models.CharField(max_length = 100)
    slug =  models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    def __str__(self):
        return self.title

    def snippet(self):
        return self.body[:50] + '...'

class Course(models.Model):
    title = models.CharField(max_length=255)
    url = models.URLField(unique=True)

    def __str__(self):
        return self.title

class Review(models.Model):
    name = models.CharField(max_length=255)
    comment = models.TextField(blank=True, default='')
    rating= models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return '{0.rating} by {0.email} for {0.course}'.format(self)
