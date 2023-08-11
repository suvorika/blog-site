# Generated by Django 4.2.4 on 2023-08-11 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-time_create', '-fixed'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
        migrations.RemoveIndex(
            model_name='article',
            name='app_article_fixed_e300bf_idx',
        ),
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, unique=True, verbose_name='Альт.название'),
        ),
        migrations.AddIndex(
            model_name='article',
            index=models.Index(fields=['-time_create', '-fixed'], name='app_article_time_cr_a1fcc0_idx'),
        ),
    ]