# Generated by Django 4.2.6 on 2023-11-01 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_mission_bba_bba_comment_bba_bba_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bba',
            name='bba_comment',
        ),
        migrations.RemoveField(
            model_name='civil',
            name='civil_comment',
        ),
        migrations.RemoveField(
            model_name='cse',
            name='cse_comment',
        ),
        migrations.RemoveField(
            model_name='eee',
            name='eee_comment',
        ),
        migrations.RemoveField(
            model_name='eng',
            name='eng_comment',
        ),
        migrations.RemoveField(
            model_name='law',
            name='law_comment',
        ),
        migrations.RemoveField(
            model_name='pharmacy',
            name='pharmacy_comment',
        ),
    ]
