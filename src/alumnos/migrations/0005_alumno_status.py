# Generated by Django 4.0 on 2022-01-21 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0004_alumno_date_create_alumno_last_update_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='status',
            field=models.CharField(choices=[('A', 'Activo'), ('B', 'Baja'), ('C', 'Cursando')], default='A', max_length=4, verbose_name='Estado'),
        ),
    ]
