# Generated by Django 4.1 on 2024-09-30 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0006_remove_tweet_links'),
    ]

    operations = [
        migrations.AddField(
            model_name='link',
            name='like',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
