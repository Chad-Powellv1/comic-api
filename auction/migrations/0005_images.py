# Generated by Django 4.0.4 on 2022-05-01 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_contributor'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cover_image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
