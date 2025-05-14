# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import JSONField

class FirstVariantBd(models.Model):
    name_object = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    competentions = models.TextField(blank=True, null=True)
    profile = models.CharField(max_length=255, blank=True, null=True)
    direction_of_preparation = models.CharField(max_length=255, blank=True, null=True)  # Добавлено
    edu_program = models.CharField(max_length=255, blank=True, null=True)  # Добавлено
    test_obj = models.CharField(max_length=50, blank=True, null=True)
    exam = models.CharField(max_length=50, blank=True, null=True)
    control_work = models.CharField(max_length=50, blank=True, null=True)
    test_obj_with_mark = models.CharField(max_length=50, blank=True, null=True)
    course_work = models.CharField(max_length=50, blank=True, null=True)
    course_project = models.CharField(max_length=50, blank=True, null=True)
    essay = models.CharField(max_length=50, blank=True, null=True)
    calcul_analytic_work = models.CharField(max_length=50, blank=True, null=True)
    creative_homework = models.CharField(max_length=50, blank=True, null=True)
    project_work = models.CharField(max_length=50, blank=True, null=True)
    classroom_hours = models.IntegerField(blank=True, null=True)
    lectures = models.IntegerField(blank=True, null=True)
    seminars = models.IntegerField(blank=True, null=True)
    independent_work = models.IntegerField(blank=True, null=True)
    ECTS = models.FloatField(blank=True, null=True)
    total_hours = models.IntegerField(blank=True, null=True)
    scientific_speciality = models.CharField(max_length=255, blank=True, null=True)  # Добавлено

    def __str__(self):
        return self.name_object

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        #db_table = 'FirstVariantBd'
        verbose_name = 'Планы'
        verbose_name_plural = 'Планы'

class Description_of_competencies(models.Model):
    competency_name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.competency_name

    class Meta:
        verbose_name = 'Компетенции'
        verbose_name_plural = 'Компетенции'

class UserSessionData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    data = models.JSONField()  # JSONField — сессия целиком
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Сессия {self.user.username} от {self.created_at}"