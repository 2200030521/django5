# Generated by Django 5.0 on 2024-03-08 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facultymodule', '0002_rename_course_id_coursedetails_courseid_and_more'),
        ('studentmodule', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='courseapplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('certificate', models.FileField(upload_to='certificate/')),
                ('coursedetails', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='facultymodule.coursedetails')),
            ],
        ),
    ]