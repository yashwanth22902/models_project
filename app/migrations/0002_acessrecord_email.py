# Generated by Django 4.2.6 on 2023-12-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='acessrecord',
            name='email',
            field=models.EmailField(default='yashwanthreddyramireddy@gmail.com', max_length=254),
        ),
    ]