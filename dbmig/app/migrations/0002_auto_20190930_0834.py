# Generated by Django 2.2.4 on 2019-09-30 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='usrd_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]