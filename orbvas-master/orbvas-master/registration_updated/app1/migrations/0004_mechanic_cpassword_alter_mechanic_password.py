# Generated by Django 4.2 on 2023-10-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechanic',
            name='cpassword',
            field=models.CharField(max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='mechanic',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
