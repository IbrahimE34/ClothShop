# Generated by Django 5.2 on 2025-04-10 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_cloth_brand_alter_cloth_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cloth',
            name='brand',
            field=models.CharField(max_length=25),
        ),
    ]
