# Generated by Django 5.1 on 2025-01-26 23:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0003_alter_membroequipe_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='membroequipe',
            name='photo',
            field=models.ImageField(blank=True, default='fotos_membros/media/fotos_membros/default.png', null=True, upload_to='fotos_membros/'),
        ),
    ]
