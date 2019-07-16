# Generated by Django 2.2.1 on 2019-07-09 06:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('RetinaScrApp', '0003_auto_20190709_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithm',
            name='doctor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='RetinaScrApp.Doctor'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='fovea_algo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fovea', to='RetinaScrApp.Algorithm'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='lesion_algo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lesion', to='RetinaScrApp.Algorithm'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='optic_algo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='optic', to='RetinaScrApp.Algorithm'),
        ),
        migrations.AlterField(
            model_name='diagnosis',
            name='vessel_algo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vessel', to='RetinaScrApp.Algorithm'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='RetinaScrApp.Doctor'),
        ),
    ]