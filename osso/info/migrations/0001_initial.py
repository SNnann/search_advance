# Generated by Django 3.0.3 on 2020-02-16 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AllData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_name', models.CharField(max_length=100)),
                ('data_category', models.CharField(max_length=100)),
                ('data_detial', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
