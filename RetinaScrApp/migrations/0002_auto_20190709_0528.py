# Generated by Django 2.2.1 on 2019-07-09 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RetinaScrApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('algo_id', models.AutoField(primary_key=True, serialize=False)),
                ('record_date', models.DateField()),
                ('algo_type', models.CharField(max_length=10)),
                ('algo_status', models.CharField(max_length=10)),
                ('last_modified', models.DateField()),
                ('doctor', models.ForeignKey(on_delete=None, to='RetinaScrApp.Doctor')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(default=None, on_delete=None, to='RetinaScrApp.Doctor'),
        ),
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('diagnosis_id', models.AutoField(primary_key=True, serialize=False)),
                ('record_date', models.DateField()),
                ('final_result', models.CharField(max_length=24)),
                ('doctor', models.ForeignKey(on_delete=None, to='RetinaScrApp.Doctor')),
                ('fovea_algo', models.ForeignKey(on_delete=None, related_name='fovea', to='RetinaScrApp.Algorithm')),
                ('lesion_algo', models.ForeignKey(on_delete=None, related_name='lesion', to='RetinaScrApp.Algorithm')),
                ('optic_algo', models.ForeignKey(on_delete=None, related_name='optic', to='RetinaScrApp.Algorithm')),
                ('patient', models.ForeignKey(on_delete=None, to='RetinaScrApp.Patient')),
                ('vessel_algo', models.ForeignKey(on_delete=None, related_name='vessel', to='RetinaScrApp.Algorithm')),
            ],
        ),
    ]
