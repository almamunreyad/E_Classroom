# Generated by Django 4.2.6 on 2023-11-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('library_img', models.ImageField(upload_to='media/library/')),
                ('library_book', models.CharField(max_length=150)),
                ('library_author', models.CharField(max_length=120)),
                ('library_file', models.FileField(upload_to='media/library/')),
            ],
        ),
    ]
