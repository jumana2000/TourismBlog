# Generated by Django 3.2.7 on 2021-10-17 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelapp', '0004_testimonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='footer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('footer_img', models.ImageField(upload_to='picture')),
            ],
        ),
    ]