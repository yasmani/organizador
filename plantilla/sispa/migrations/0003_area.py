# Generated by Django 5.1.5 on 2025-02-11 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sispa', '0002_solicitud'),
    ]

    operations = [
        migrations.CreateModel(
            name='AREA',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identificador', models.CharField(max_length=10)),
                ('area', models.CharField(max_length=255)),
                ('perfil', models.CharField(max_length=10)),
            ],
        ),
    ]
