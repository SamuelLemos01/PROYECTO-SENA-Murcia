# Generated by Django 5.1.5 on 2025-02-17 19:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estrenos',
            name='fecha_pelicula',
            field=models.DateField(default='2000-01-01'),
        ),
        migrations.AddField(
            model_name='estrenos',
            name='nuevo',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='estrenos',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes/'),
        ),
        migrations.AlterField(
            model_name='estrenos',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='estrenos',
            name='stock',
            field=models.IntegerField(),
        ),
    ]
