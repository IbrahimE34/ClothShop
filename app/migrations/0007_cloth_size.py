# Generated by Django 5.2 on 2025-04-12 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_cloth_brand'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloth',
            name='size',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
