# Generated by Django 5.0.6 on 2024-05-31 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_application_document_student_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='state',
            field=models.IntegerField(choices=[(0, 'inward'), (1, 'outward')], default=0),
        ),
    ]
