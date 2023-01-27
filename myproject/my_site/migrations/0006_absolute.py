# Generated by Django 4.0a1 on 2021-10-16 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_site', '0005_alter_articles_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Absolute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=160)),
                ('content', models.TextField(blank=True)),
                ('slug', models.SlugField(unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Absolute list',
                'verbose_name_plural': 'Absolute Lists',
            },
        ),
    ]
