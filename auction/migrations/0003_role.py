# Generated by Django 4.0.4 on 2022-05-01 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0002_auction_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('con_role', models.CharField(blank=True, choices=[('', '----'), ('Writer', 'Writer'), ('Artist', 'Artist'), ('Penciller', 'Penciller'), ('Inker', 'Inker'), ('Colorist', 'Colorist'), ('Cover Artist', 'Cover Artist'), ('Letterer', 'Letterer'), ('Editor', 'Editor'), ('Created By', 'Created By')], max_length=12)),
            ],
        ),
    ]
