# Generated by Django 2.1.4 on 2018-12-28 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20181228_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=15),
        ),
    ]
