from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Категория')

    def get_absolute_url(self):
        return reverse('view_by_category', kwargs={"category_id": self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']


class News(models.Model):
    title = models.CharField(max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT, null=True)
    views_quantity = models.IntegerField(default=0)
    rating_sum = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse('view_news', kwargs={'news_id': self.pk})

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        # ordering = ['-created_at']

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Rating(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)

    class Meta:
        unique_together = [['owner', 'news']]
        verbose_name = 'Рейтинг'
        verbose_name_plural = 'Рейтинги'


class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return f'{self.owner} - {self.news}'


