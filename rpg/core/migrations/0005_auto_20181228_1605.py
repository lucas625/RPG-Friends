# Generated by Django 2.1.4 on 2018-12-28 19:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20181228_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monstro',
            name='classe',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.Classe'),
        ),
    ]
