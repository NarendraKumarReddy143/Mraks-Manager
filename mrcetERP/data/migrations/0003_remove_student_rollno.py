# Generated by Django 4.1.7 on 2024-03-01 08:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_student_branch_student_rollno_student_year'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='rollno',
        ),
    ]
