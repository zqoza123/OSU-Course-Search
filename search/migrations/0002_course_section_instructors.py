# Generated by Django 4.2.1 on 2023-05-06 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_section',
            name='instructors',
            field=models.ManyToManyField(to='search.instructor'),
        ),
    ]
