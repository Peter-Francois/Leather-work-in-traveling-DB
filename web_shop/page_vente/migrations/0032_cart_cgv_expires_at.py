# Generated by Django 5.1.2 on 2025-03-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page_vente', '0031_privacypolicy'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='cgv_expires_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
