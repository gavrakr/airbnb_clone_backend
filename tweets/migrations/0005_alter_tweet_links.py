# Generated by Django 4.1 on 2024-09-30 16:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0004_alter_tweet_links'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='links',
            field=models.ManyToManyField(related_name='tweets', to='tweets.link'),
        ),
    ]
