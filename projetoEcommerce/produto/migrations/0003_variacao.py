# Generated by Django 3.0.6 on 2020-06-03 12:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0002_auto_20200603_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='Variacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(blank=True, max_length=50, null=True)),
                ('preco', models.FloatField()),
                ('preco_promocional', models.FloatField(default=0)),
                ('estoque', models.PositiveIntegerField(default=1)),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='produto.Produto')),
            ],
        ),
    ]
