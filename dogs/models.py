from django.db import models


class Breed(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Название породы",
        help_text="Укажите название породы",
    )
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="Описание породы",
        help_text="Укажите описание породы",
    )

    class Meta:
        verbose_name = "Порода"
        verbose_name_plural = "Породы"


class Dog(models.Model):
    name = models.CharField(
        max_length=100, verbose_name="Кличка", help_text="Укажите кличку"
    )
    breed = models.ForeignKey(
        Breed,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Порода",
        help_text="Выберите породу",
    )
    photo = models.ImageField(
        upload_to="dogs/photo",
        verbose_name="Фото",
        help_text="Загрузите фото собаки",
        blank=True,
        null=True,
    )
    date_born = models.DateField(
        verbose_name="Дата рождения",
        help_text="Укажите дату рождения",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = "Собака"
        verbose_name_plural = "Собаки"
