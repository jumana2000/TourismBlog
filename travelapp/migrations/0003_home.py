# Generated by Django 3.2.7 on 2021-10-17 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0002_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_img', models.ImageField(upload_to='picture')),
            ],
        ),
    ]
