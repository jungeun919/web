# Generated by Django 3.1 on 2021-02-24 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qna', '0004_auto_20210221_0035'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='post',
            name='writer',
            field=models.CharField(max_length=50),
        ),
    ]
