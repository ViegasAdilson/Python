# Generated by Django 3.0.7 on 2020-06-11 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0007_auto_20200604_1354'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='descricao_lona',
            new_name='descricao_longa',
        ),
    ]
