# Generated by Django 4.1 on 2022-08-23 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='body',
            field=models.TextField(blank=True, null=True),
        ),
    ]
