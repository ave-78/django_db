# Generated by Django 2.2.4 on 2019-08-19 15:50

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=datetime.datetime(2019, 8, 19, 15, 50, 12, 824535, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('created', models.DateTimeField(default=datetime.datetime(2019, 8, 19, 15, 50, 12, 826535, tzinfo=utc))),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_test.User')),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_test.Blog')),
                ('likes', models.ManyToManyField(related_name='likes', to='db_test.User')),
            ],
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='db_test.User'),
        ),
        migrations.AddField(
            model_name='blog',
            name='subscribers',
            field=models.ManyToManyField(related_name='subscriptions', to='db_test.User'),
        ),
    ]
