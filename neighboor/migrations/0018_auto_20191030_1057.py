# Generated by Django 2.2.6 on 2019-10-30 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighboor', '0017_auto_20191030_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neighborhood',
            name='health_department_contact',
            field=models.IntegerField(max_length=255),
        ),
        migrations.AlterField(
            model_name='neighborhood',
            name='police_authority_contact',
            field=models.IntegerField(max_length=255),
        ),
    ]