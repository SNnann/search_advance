# Generated by Django 3.0.3 on 2020-03-29 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0006_auto_20200219_1050'),
    ]

    operations = [
        migrations.AddField(
            model_name='level',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 29, 21, 28, 11, 461624)),
        ),
        migrations.AddField(
            model_name='level',
            name='level_role',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='level',
            name='level_route',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='document',
            name='group',
            field=models.CharField(choices=[('อาหาร', 'อาหาร'), ('วัตถุอันตราย', 'วัตถุอันตราย'), ('วัตถุออกฤทธิ์-วัตถุเสพติด', 'วัตถุออกฤทธิ์-วัตถุเสพติด'), ('ยา', 'ยา'), ('เครื่องสำอาง', 'เครื่องสำอาง'), ('เครื่องมือแพทย์', 'เครื่องมือแพทย์')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='level',
            name='group',
            field=models.CharField(choices=[('อาหาร', 'อาหาร'), ('วัตถุอันตราย', 'วัตถุอันตราย'), ('วัตถุออกฤทธิ์-วัตถุเสพติด', 'วัตถุออกฤทธิ์-วัตถุเสพติด'), ('ยา', 'ยา'), ('เครื่องสำอาง', 'เครื่องสำอาง'), ('เครื่องมือแพทย์', 'เครื่องมือแพทย์')], default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='level',
            name='level_name',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AlterField(
            model_name='level',
            name='level_ref',
            field=models.CharField(default='', max_length=500),
        ),
    ]
