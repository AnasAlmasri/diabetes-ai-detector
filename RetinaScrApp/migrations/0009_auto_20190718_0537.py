# Generated by Django 2.2.1 on 2019-07-18 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RetinaScrApp', '0008_doctor_doc_username'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='algorithm',
            name='record_date',
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='last_modified',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='algorithm',
            name='source_code',
            field=models.CharField(default=None, max_length=200000),
        ),
    ]
