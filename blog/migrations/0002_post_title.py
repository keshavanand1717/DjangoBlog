# Generated by Django 4.1.5 on 2023-01-19 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default='abc', max_length=100),
            preserve_default=False,
        ),
    ]
