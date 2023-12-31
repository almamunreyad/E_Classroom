# Generated by Django 4.2.6 on 2023-10-19 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_about_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category_Cse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Cse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cse_img', models.ImageField(upload_to='media/cse/')),
                ('cse_book', models.CharField(max_length=150)),
                ('cse_teacher', models.CharField(max_length=120)),
                ('cse_file', models.FileField(upload_to='media/cse/')),
            ],
        ),
    ]
