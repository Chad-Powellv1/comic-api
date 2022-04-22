# Generated by Django 4.0.4 on 2022-04-21 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detail',
            name='issue_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='review',
            name='rate',
            field=models.IntegerField(choices=[(5, 5), (4, 4), (3, 3), (2, 2), (1, 1), (0, 0)], default=None),
        ),
    ]