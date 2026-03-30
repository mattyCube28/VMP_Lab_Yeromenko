from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=150, verbose_name="ПІБ")
    group = models.CharField(max_length=50, verbose_name="Група")
    math_grade = models.IntegerField(verbose_name="Оцінка з математики")
    programming_grade = models.IntegerField(verbose_name="Оцінка з програмування")
    english_grade = models.IntegerField(verbose_name="Оцінка з англійської")
    contact_info = models.CharField(max_length=255, blank=True, null=True, verbose_name="Контакти")
    photo = models.ImageField(upload_to='photos/', blank=True, null=True, verbose_name="Фото")
    def __str__(self):
        return f"{self.full_name} ({self.group})"