# Generated by Django 3.0.6 on 2020-05-18 18:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainWeb', '0006_auto_20200518_1752'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='news_id',
        ),
        migrations.AddField(
            model_name='news',
            name='comments',
            field=models.ManyToManyField(blank=True, to='MainWeb.Comment', verbose_name='Холбогдох Сэтгэгдэлийн Жагсаалт'),
        ),
    ]