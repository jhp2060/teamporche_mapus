# Generated by Django 2.2.6 on 2019-11-05 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('building_map', '0010_auto_20191105_2157'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facility',
            name='type',
            field=models.CharField(choices=[('정수기', '정수기'), ('인쇄기', '인쇄기'), ('소화기', '소화기'), ('화장실', '화장실'), ('수면실', '수면실'), ('샤워실', '샤워실')], default=None, max_length=3),
        ),
    ]
