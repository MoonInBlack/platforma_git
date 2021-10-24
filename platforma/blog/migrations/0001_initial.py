# Generated by Django 3.2.6 on 2021-08-15 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tiitle', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('author', models.CharField(max_length=100)),
                ('content', models.TextField(blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Опубликованно')),
                ('photo', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('views', models.IntegerField(default=0, verbose_name='Кол-во просмотров')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='post', to='blog.category')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
