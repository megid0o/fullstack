from django.db import models
from pytils.translit import slugify

class Category(models.Model):
   name = models.CharField("Название категории",max_length=255)
   slug = models.SlugField(unique=True, blank=True,editable=False)

   class Meta:
      verbose_name = "Категория"
      verbose_name_plural = "Категории"

   def __str__(self):
      return self.name

   
   def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super().save(*args, **kwargs)


class Job(models.Model):
   title = models.CharField("Название работы", max_length=255)
   category = models.ForeignKey("Category", verbose_name="Категория", on_delete=models.CASCADE)
   company = models.CharField("Название компании", max_length=80)
   experiences = models.PositiveIntegerField("Опыт работы в  годах",max_length=89,default="Без опыта")
   salary = models.PositiveIntegerField("Оклад",max_length=89)
   description = models.TextField("Описание работы")
   skills = models.CharField("Необходимые навыки", max_length=255)
   adress = models.CharField("Адрес работы", max_length=100,default="адрес компании")
   phone = models.CharField("номер телефона", max_length=100)
   email = models.EmailField("Электронная почта", max_length=255)

   class Meta:
      verbose_name = "Работа"
      verbose_name_plural = "Работы"

   def __str__(self):
      return self.title



class Vacancy(models.Model):
   title = models.CharField("Название вакансии", max_length=255)
   description = models.TextField("Описание вакансии")
   company = models.CharField("Название компании", max_length=80)
   location = models.CharField("Местоположение вакансии", max_length=100)
   date_posted = models.DateTimeField("Дата публикации", auto_now_add=True)


