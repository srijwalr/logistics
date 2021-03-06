# Generated by Django 2.2.4 on 2019-11-29 12:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cosingnormaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consgnrm_code', models.CharField(blank=True, max_length=50, null=True)),
                ('consgnrm_clntmaspntr', models.IntegerField(blank=True, null=True)),
                ('consgnrm_whmcode', models.IntegerField(blank=True, null=True)),
                ('consgnrm_name', models.CharField(blank=True, max_length=100, null=True)),
                ('consgnrm_address', models.CharField(blank=True, max_length=400, null=True)),
                ('cosngnrm_desc', models.CharField(blank=True, max_length=250, null=True)),
                ('cosngnrm_slno', models.IntegerField(blank=True, null=True)),
                ('consgnrm_remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('consgnrm_active', models.CharField(blank=True, max_length=1, null=True)),
                ('consgnrm_makerid', models.IntegerField(blank=True, null=True)),
                ('consgnrm_maketime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Freightforroute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fght_fretypeptr', models.IntegerField(blank=True, null=True, verbose_name='Code')),
                ('fght_routeptr', models.IntegerField(blank=True, null=True, verbose_name='Route type')),
                ('fght_basefreight', models.IntegerField(blank=True, null=True, verbose_name='Base Freight')),
                ('fght_kmrate', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='KM Rate')),
                ('fght_vehcatptr', models.IntegerField(blank=True, null=True, verbose_name='Vehicle Category')),
                ('fght_slno', models.IntegerField(blank=True, null=True, verbose_name='Serial no.')),
                ('fght_remarks', models.CharField(blank=True, max_length=250, null=True, verbose_name='Remarks')),
                ('fght_active', models.CharField(blank=True, max_length=1, null=True, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Freighttypes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fretype_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Code')),
                ('fretype_desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description')),
                ('fretype_slno', models.IntegerField(blank=True, null=True, verbose_name='Serial no.')),
                ('fretype_remarks', models.CharField(blank=True, max_length=250, null=True, verbose_name='Remarks')),
                ('fretype_active', models.CharField(blank=True, max_length=1, null=True, verbose_name='Status')),
                ('fretype_nnc_code', models.CharField(blank=True, max_length=10, null=True)),
                ('fretype_whmcode', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('procat_code', models.CharField(blank=True, max_length=25, null=True, verbose_name='Code')),
                ('procat_desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description')),
                ('procat_slno', models.IntegerField(blank=True, null=True, verbose_name='Serial no.')),
                ('procat_active', models.CharField(blank=True, max_length=1, null=True, verbose_name='Status')),
                ('procat_remarks', models.CharField(blank=True, max_length=250, null=True, verbose_name='Remarks')),
                ('procat_makerid', models.IntegerField(blank=True, null=True)),
                ('procat_maketime', models.DateTimeField(blank=True, null=True)),
                ('procat_clntpntr', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Productgroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prog_code', models.CharField(blank=True, max_length=50, null=True)),
                ('prog_desc', models.CharField(blank=True, max_length=150, null=True)),
                ('prog_slno', models.IntegerField(blank=True, null=True)),
                ('prog_rmrks', models.TextField(blank=True, null=True)),
                ('prog_status', models.CharField(blank=True, max_length=1, null=True)),
                ('prog_clntpntr', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Routemaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rtm_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Code')),
                ('rtm_desc', models.CharField(max_length=100, verbose_name='Description')),
                ('rtm_dist', models.CharField(max_length=50, verbose_name='Distance')),
                ('rtm_slno', models.IntegerField(blank=True, null=True, verbose_name='Serial no.')),
                ('rtm_remarks', models.CharField(blank=True, max_length=250, null=True, verbose_name='Remarks')),
                ('rtm_active', models.CharField(blank=True, max_length=1, null=True, verbose_name='Status')),
                ('rtm_details', models.CharField(blank=True, max_length=250, null=True, verbose_name='Details')),
            ],
        ),
        migrations.CreateModel(
            name='Vehiclecategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehcat_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Code')),
                ('vehcat_desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description')),
                ('vehcat_wtcapacity', models.FloatField(blank=True, null=True, verbose_name='Weight capacity')),
                ('vehcat_length', models.FloatField(blank=True, null=True, verbose_name='Length')),
                ('vehcat_width', models.FloatField(blank=True, null=True, verbose_name='Width')),
                ('vehcat_ft', models.CharField(blank=True, max_length=50, null=True)),
                ('vehcat_kmrate', models.DecimalField(blank=True, decimal_places=2, max_digits=18, null=True, verbose_name='KM Rate')),
                ('vehcat_slno', models.IntegerField(blank=True, null=True, verbose_name='Serial no.')),
                ('vehcat_active', models.CharField(blank=True, max_length=1, null=True)),
                ('vehcat_remarks', models.CharField(blank=True, max_length=250, null=True, verbose_name='Remarks')),
                ('vehcat_makerid', models.IntegerField(blank=True, null=True)),
                ('vehcat_maketime', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiclemaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehmas_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Vehicle Number')),
                ('vehmas_desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description')),
                ('vehmas_drivername', models.CharField(blank=True, max_length=20, null=True, verbose_name='Driver Name')),
                ('vehmas_phone', models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number')),
                ('vehmas_modepntr', models.IntegerField(blank=True, null=True)),
                ('vehmas_slno', models.IntegerField(blank=True, null=True)),
                ('vehmas_active', models.CharField(blank=True, max_length=1, null=True, verbose_name='Status')),
                ('vehmas_remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('vehmas_makerid', models.IntegerField(blank=True, null=True)),
                ('vehmas_maketime', models.DateTimeField(blank=True, null=True)),
                ('vehmas_clntpntr', models.IntegerField(blank=True, null=True)),
                ('vehmas_catpntr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Vehiclecategory', verbose_name='Category')),
                ('vehmas_frtyppntr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Freighttypes', verbose_name='Vehicle Mode')),
            ],
        ),
        migrations.CreateModel(
            name='Productsubcategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('proscat_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Code')),
                ('proscat_desc', models.CharField(blank=True, max_length=100, null=True, verbose_name='Description')),
                ('proscat_volume', models.FloatField(blank=True, null=True, verbose_name='Volume')),
                ('proscat_weight', models.FloatField(blank=True, null=True, verbose_name='Weight')),
                ('proscat_width', models.FloatField(blank=True, null=True, verbose_name='Width')),
                ('proscat_length', models.FloatField(blank=True, null=True, verbose_name='Length')),
                ('proscat_slno', models.IntegerField(blank=True, null=True, verbose_name='Serial no.')),
                ('proscat_active', models.CharField(blank=True, max_length=1, null=True, verbose_name='Status')),
                ('proscat_remarks', models.CharField(blank=True, max_length=250, null=True, verbose_name='Remarks')),
                ('proscat_makerid', models.IntegerField(blank=True, null=True)),
                ('proscat_maketime', models.DateTimeField(blank=True, null=True)),
                ('proscat_clntcode', models.IntegerField(blank=True, null=True)),
                ('proscat_procatpntr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Productcategory', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Productmaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promas_code', models.CharField(blank=True, max_length=50, null=True, verbose_name='Code')),
                ('promas_desc', models.CharField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('promas_quantity', models.IntegerField(blank=True, null=True, verbose_name='Quantity')),
                ('promas_slno', models.IntegerField(blank=True, null=True, verbose_name='Serial no.')),
                ('promas_active', models.CharField(blank=True, max_length=1, null=True, verbose_name='Status')),
                ('promas_remarks', models.CharField(blank=True, max_length=250, null=True, verbose_name='Remarks')),
                ('promas_makerid', models.IntegerField(blank=True, null=True)),
                ('promas_maketime', models.DateTimeField(blank=True, null=True)),
                ('promas_clntcode', models.IntegerField(blank=True, null=True)),
                ('promas_group_pntr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Productgroup')),
                ('promas_procat_pntr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Productcategory', verbose_name='Category')),
                ('promas_proscat_pntr', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='master.Productsubcategory', verbose_name='Sub category')),
            ],
        ),
        migrations.CreateModel(
            name='Cosingneemaster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consgnem_code', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name='Consignee code')),
                ('consgnem_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Consignee name')),
                ('consgnem_branch', models.CharField(blank=True, max_length=50, null=True, verbose_name='Consignee branch')),
                ('consgnem_address', models.CharField(blank=True, max_length=500, null=True, verbose_name='Consignee address')),
                ('consgnem_city', models.CharField(blank=True, max_length=50, null=True, verbose_name='Consignee city')),
                ('consgnem_district', models.CharField(blank=True, max_length=50, null=True, verbose_name='Consignee district')),
                ('consgnem_pincode', models.IntegerField(blank=True, null=True, verbose_name='Consignee pincode')),
                ('consgnem_routtyp', models.CharField(blank=True, max_length=20, null=True, verbose_name='Consignee route type')),
                ('consgnem_gsttin', models.CharField(blank=True, max_length=25, null=True, verbose_name='Consignee GST')),
                ('consgnem_pan', models.CharField(blank=True, max_length=25, null=True, verbose_name='Consignee PAN')),
                ('consgnem_distance', models.FloatField(blank=True, null=True, verbose_name='Consignee distance')),
                ('cosngnrm_slno', models.IntegerField(blank=True, null=True)),
                ('consgnem_remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('consgnem_active', models.CharField(blank=True, max_length=1, null=True)),
                ('consgnem_makerid', models.IntegerField(blank=True, null=True)),
                ('consgnem_maketime', models.DateTimeField(blank=True, null=True)),
                ('consgnem_clntpntr', models.IntegerField(blank=True, null=True)),
                ('consgnem_routepntr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='master.Routemaster')),
            ],
        ),
    ]
