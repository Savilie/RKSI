
from django.db import models
from django.urls import reverse

from django.utils.text import slugify
from pytils.translit import slugify as pytils_slugify

class Students(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    speciality = models.ForeignKey('Articles', on_delete=models.SET_NULL, related_name='speciality', verbose_name='Специальность')
    group = models.ForeignKey('Groups', on_delete=models.SET_NULL, related_name='group', verbose_name='Группа')
    group_lead = models.ForeignKey('Teacher', on_delete=models.SET_NULL , related_name='group_lead', verbose_name='Классный руководитель')
    edu_price = models.ForeignKey('EduPrice', on_delete=models.SET_NULL, related_name='edu_price', verbose_name='Форма финансирования обучения')
    edu_form = models.ForeignKey('EduForm', on_delete=models.SET_NULL, related_name='edu_form', verbose_name='Форма обучения')
    health = models.ForeignKey('Health', on_delete=models.SET_NULL, related_name='health_group', verbose_name='Группа здоровья')
    social = models.ForeignKey('Social', on_delete=models.SET_NULL, verbose_name='Социальный статус')
    photo = models.ImageField(upload_to='photos/%Y/%m/&d', null=True, verbose_name='Фото')

    class Meta:
        verbose_name = 'Студенты'
        verbose_name_plural = 'Студенты'

class Groups(models.Model):
    groups = models.CharField(max_length=15, verbose_name='Группа')
    members = models.ForeignKey('Students', on_delete=models.SET_NULL, related_name='members', verbose_name='Состав группы')

class Speciality(models.Model):
    spec_name = models.CharField(max_length=255, verbose_name='Специальность')

class Social(models.Model):
    statuses = models.CharField(max_length=255, verbose_name='Социальный статус')

class EduPrice(models.Model):
    edu_price = models.CharField(max_length=255, verbose_name='Форма финансирования обучения')

class Health(models.Model):
    health_groups = models.IntegerField(max_length=1, verbose_name='Группа здоровья')

class EduForm(models.Model):
    edu_form = models.CharField(max_length=255, verbose_name='Форма обучения')


class Enrollee(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    photo = models.ImageField(upload_to='photos/%Y/%m/&d', null=True, verbose_name='Фото')
    """Дописать"""


class Teacher(models.Model):
    full_name = models.CharField(max_length=255, verbose_name='ФИО')
    photo = models.ImageField(upload_to='photos/%Y/%m/&d', null=True, verbose_name='Фото')
    """Дописать"""


class Articles(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    subtitle = models.CharField(max_length=255, verbose_name='Подзаголовок')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='Ссылка на новость')
    content = models.TextField(blank=True, verbose_name='Содержание')
    photo_url = models.URLField()
    photo = models.ForeignKey('Articles', on_delete=models.SET_NULL, related_name='Фото')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    is_published = models.BooleanField(default=True, verbose_name='Статус публикации')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
        ordering = ['time_create',]

    def save(self, *args, **kwargs):
        self.slug = slugify(pytils_slugify(self.title))
        super().save(*args, **kwargs)

class Photo(models.Model):
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', null=True, verbose_name='Фото')
