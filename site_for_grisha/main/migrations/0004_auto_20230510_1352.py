# Generated by Django 3.2.18 on 2023-05-10 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20230510_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='covers',
            name='creator',
            field=models.CharField(error_messages={'required': ''}, max_length=20, null=True, verbose_name='Исполнитель'),
        ),
        migrations.AlterField(
            model_name='covers',
            name='file',
            field=models.FileField(error_messages={'required': ''}, null=True, upload_to='..\\media'),
        ),
        migrations.AlterField(
            model_name='covers',
            name='title',
            field=models.CharField(error_messages={'required': ''}, max_length=50, null=True, verbose_name='Название'),
        ),
    ]
