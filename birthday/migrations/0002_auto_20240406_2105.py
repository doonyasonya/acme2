# Generated by Django 3.2.16 on 2024-04-06 18:05

import birthday.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='birthday',
            name='image',
            field=models.ImageField(blank=True, upload_to='birthdays_images', verbose_name='Фото'),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='birthday',
            field=models.DateField(validators=[birthday.validators.real_age], verbose_name='Дата рождения'),
        ),
        migrations.AlterField(
            model_name='birthday',
            name='last_name',
            field=models.CharField(blank=True, help_text='Опциональное поле', max_length=20, verbose_name='Фамилия'),
        ),
        migrations.AddConstraint(
            model_name='birthday',
            constraint=models.UniqueConstraint(fields=('first_name', 'last_name', 'birthday'), name='Unique person constraint'),
        ),
    ]
