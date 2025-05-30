# Generated by Django 5.1.2 on 2025-02-06 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_vente', '0008_alter_macrame_lien_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='macrame',
            old_name='lien_image',
            new_name='lien_image1',
        ),
        migrations.RemoveField(
            model_name='macrame',
            name='disponible',
        ),
        migrations.AddField(
            model_name='macrame',
            name='lien_image2',
            field=models.URLField(default='', max_length=20000),
        ),
        migrations.AddField(
            model_name='macrame',
            name='lien_image3',
            field=models.URLField(default='', max_length=20000),
        ),
        migrations.AddField(
            model_name='macrame',
            name='lien_image4',
            field=models.URLField(default='', max_length=20000),
        ),
        migrations.AddField(
            model_name='macrame',
            name='stock',
            field=models.IntegerField(default=0),
        ),
    ]
