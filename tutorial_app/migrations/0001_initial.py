# Generated by Django 3.2.4 on 2021-06-20 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('english', models.CharField(blank=True, default='', max_length=250)),
                ('russian', models.CharField(blank=True, default='', max_length=250)),
                ('turkmen', models.CharField(blank=True, default='', max_length=250)),
                ('turkish', models.CharField(blank=True, default='', max_length=250)),
            ],
            options={
                'ordering': ('english',),
            },
        ),
    ]
