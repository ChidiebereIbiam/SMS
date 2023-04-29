# Generated by Django 4.2 on 2023-04-29 00:01

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentuser',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='current_class',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='current_status',
            field=models.CharField(blank=True, choices=[('active', 'Active'), ('inactive', 'Inactive')], default='active', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='date_of_admission',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='date_of_birth',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female')], default='male', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='others',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='parent_mobile_number',
            field=models.CharField(blank=True, max_length=13, null=True, validators=[django.core.validators.RegexValidator(message="Entered mobile number isn't in a right format!", regex='^[0-9]{10,15}$')]),
        ),
        migrations.AddField(
            model_name='studentuser',
            name='passport',
            field=models.ImageField(blank=True, null=True, upload_to='students/passports/'),
        ),
        migrations.AlterField(
            model_name='studentuser',
            name='registration_number',
            field=models.CharField(editable=False, max_length=244, primary_key=True, serialize=False, unique=True),
        ),
        migrations.DeleteModel(
            name='StudentProfile',
        ),
    ]