# Generated by Django 4.2 on 2023-05-02 01:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Instructor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_photo', models.ImageField(blank=True, null=True, upload_to='instructor_profile/')),
                ('name', models.CharField(max_length=150)),
                ('headline', models.CharField(max_length=150)),
                ('about', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Course_Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('course', models.CharField(max_length=250)),
                ('file', models.FileField(upload_to='course_content/')),
                ('instructor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.instructor')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
                ('langauge', models.CharField(max_length=255)),
                ('course_highlight', models.TextField()),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('instructor', models.ManyToManyField(related_name='instructors', to='api.instructor')),
                ('modules', models.ManyToManyField(related_name='sections', to='api.course_module')),
            ],
        ),
    ]