# Generated by Django 4.2.3 on 2023-08-09 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_alter_person_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('slug', models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name='person',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]
