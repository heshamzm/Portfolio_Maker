# Generated by Django 3.2.8 on 2021-12-27 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Portfolio', '0005_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='plan',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='story',
            field=models.CharField(max_length=500, null=True),
        ),
    ]