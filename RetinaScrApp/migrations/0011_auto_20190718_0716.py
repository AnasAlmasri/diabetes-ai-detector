# Generated by Django 2.2.1 on 2019-07-18 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RetinaScrApp', '0010_remove_algorithm_algo_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithm',
            name='last_modified',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
