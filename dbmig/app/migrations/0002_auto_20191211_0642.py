# Generated by Django 2.2.4 on 2019-12-11 06:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lrtranslink',
            name='trans_consgnepntr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Cosingneemaster'),
        ),
        migrations.AlterField(
            model_name='lrtranslink',
            name='trans_productpntr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Productmaster'),
        ),
        migrations.AlterField(
            model_name='lrtranslink',
            name='trans_whmpntr',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Companywarehousemaster'),
        ),
    ]