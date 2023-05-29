# Generated by Django 4.2.1 on 2023-05-29 15:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='id',
            field=models.UUIDField(default=uuid.UUID('60b83ca2-3d17-4035-a34e-1076e926a74b'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='productformainpage',
            name='pic',
            field=models.FileField(upload_to='main/static/main/img', verbose_name='img'),
        ),
    ]
