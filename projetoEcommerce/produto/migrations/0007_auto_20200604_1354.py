# Generated by Django 3.0.6 on 2020-06-04 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0006_auto_20200604_1336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produto',
            old_name='preco_marking',
            new_name='preco_marketing',
        ),
        migrations.RenameField(
            model_name='produto',
            old_name='peco_marking_promocional',
            new_name='preco_marketing_promocional',
        ),
    ]