# Generated by Django 4.2.6 on 2023-10-19 10:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_category_cse_cse'),
    ]

    operations = [
        migrations.AddField(
            model_name='cse',
            name='category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.category_cse'),
        ),
    ]