# Generated by Django 4.2.5 on 2023-10-16 15:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yousta', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cloths',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='yousta.category'),
        ),
    ]