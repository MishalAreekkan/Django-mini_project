# Generated by Django 5.0.4 on 2024-04-12 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_user_login_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='unversity',
            name='place',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='unversity',
            name='teachers',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='unversity',
            name='department',
            field=models.CharField(max_length=50),
        ),
    ]
