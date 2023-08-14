# Generated by Django 4.2.4 on 2023-08-14 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='ViewCount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField(verbose_name='IP адрес')),
                ('viewed_on', models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='blog.article')),
            ],
            options={
                'verbose_name': 'Просмотр',
                'verbose_name_plural': 'Просмотры',
                'ordering': ('-viewed_on',),
                'indexes': [models.Index(fields=['-viewed_on'], name='blog_viewco_viewed__0b448b_idx')],
            },
        ),
    ]
