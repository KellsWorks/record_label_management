# Generated by Django 4.1.4 on 2022-12-24 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_song_cover_art_catalogue'),
    ]

    operations = [
        migrations.RenameField(
            model_name='song',
            old_name='user',
            new_name='artist',
        ),
    ]