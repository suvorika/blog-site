# Generated by Django 4.2.4 on 2023-08-14 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('system', '0002_feedback'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='following',
            field=models.ManyToManyField(blank=True, related_name='followers', to='system.profile', verbose_name='Подписки'),
        ),
    ]
