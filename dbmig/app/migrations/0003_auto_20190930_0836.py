# Generated by Django 2.2.4 on 2019-09-30 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20190930_0834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='password',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
