# Generated by Django 4.2 on 2023-05-03 15:17

import baham.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('baham', '0002_alter_vehiclemodel_model_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vehiclemodel',
            old_name='model_id',
            new_name='make_id',
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='created_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='updated_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='vehiclemodel',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='vehiclemodel',
            name='model',
            field=models.CharField(default='Unknown', max_length=20),
        ),
        migrations.AlterField(
            model_name='vehiclemodel',
            name='type',
            field=models.CharField(choices=[('AUTO_RICKSHAW', 'Auto Rickshaw'), ('SEDAN', 'Sedan'), ('HATCHBACK', 'Hatch Back'), ('SUV', 'Sub-Urban Vehicle'), ('VAN', 'Van'), ('HIGH_ROOF', 'High Roof'), ('MOTORCYCLE', 'Moto cycle/Scooter')], help_text='Select the vehicle chassis type', max_length=50),
        ),
        migrations.AlterModelTable(
            name='vehiclemodel',
            table='baham_vehicle_model',
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('vehicle_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('registration_number', models.CharField(help_text='Unique registration/license plate no. of the vehicle.', max_length=10, unique=True)),
                ('color', models.CharField(default='white', max_length=50, validators=[baham.models.validate_color])),
                ('date_added', models.DateField(verbose_name=models.DateTimeField(default=django.utils.timezone.now, editable=False))),
                ('status', models.CharField(choices=[('AVAILABLE', 'Available'), ('FULL', 'Full'), ('INACTIVE', 'Inactive'), ('REMOVED', 'Removed')], max_length=50)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baham.vehiclemodel')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('birthdate', models.DateField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('type', models.CharField(choices=[('OWNER', 'Owner'), ('COMPANION', 'Companion')], max_length=10)),
                ('primary_contact', models.CharField(max_length=20)),
                ('alternate_contact', models.CharField(max_length=20, null=True)),
                ('address', models.CharField(max_length=255)),
                ('address_latitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('address_longitude', models.DecimalField(decimal_places=6, max_digits=9, null=True)),
                ('landmark', models.CharField(max_length=255)),
                ('town', models.CharField(choices=[('Bin Qasim', 'Bin Qasim'), ('Gadap', 'Gadap'), ('Gulberg', 'Gulberg'), ('Gulshan-e-Iqbal', 'Gulshan-e-Iqbal'), ('Jamshed', 'Jamshed'), ('Keamari', 'Keamari'), ('Korangi', 'Korangi'), ('Landhi', 'Landhi'), ('Liaquatabad', 'Liaquatabad'), ('Malir', 'Malir'), ('New Karachi', 'New Karachi'), ('North Nazimabad', 'North Nazimabad'), ('Orangi', 'Orangi'), ('SITE', 'SITE'), ('Saddar', 'Saddar'), ('Shah Faisal', 'Shah Faisal')], max_length=50)),
                ('active', models.BooleanField(default=True, editable=False)),
                ('date_deactivated', models.DateTimeField(editable=False, null=True)),
                ('bio', models.TextField()),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('contract_id', models.AutoField(db_column='id', primary_key=True, serialize=False)),
                ('effective_start_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('is_active', models.BooleanField(default=True)),
                ('fuel_share', models.PositiveSmallIntegerField(help_text='Percentage of fuel contribution')),
                ('maintenance_share', models.PositiveSmallIntegerField(help_text='Percentage of maintainance contribution')),
                ('schedule', models.JSONField()),
                ('companion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baham.userprofile')),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('updated_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baham.vehicle')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
