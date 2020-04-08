# Generated by Django 3.1 on 2020-04-08 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookmark', '0002_auto_20200408_1923'),
        ('posts', '0002_auto_20200408_1923'),
        ('streams', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bookmarks',
            field=models.ManyToManyField(to='bookmark.Bookmark'),
        ),
        migrations.AddField(
            model_name='user',
            name='posts',
            field=models.ManyToManyField(to='posts.Post'),
        ),
        migrations.AddField(
            model_name='user',
            name='streams',
            field=models.ManyToManyField(to='streams.Stream'),
        ),
    ]
