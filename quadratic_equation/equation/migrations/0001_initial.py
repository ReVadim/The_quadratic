# Generated by Django 4.0.5 on 2022-06-11 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('username', models.CharField(max_length=50, verbose_name='Пользователь')),
                ('comment_text', models.CharField(max_length=300, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='SolvingEquation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('params', models.CharField(max_length=255, verbose_name='Параметры')),
                ('results', models.CharField(max_length=255, verbose_name='Результат')),
            ],
            options={
                'verbose_name': 'Решение',
                'verbose_name_plural': 'Решения',
                'ordering': ['-created_at'],
            },
        ),
    ]
