# Generated by Django 3.2.10 on 2022-05-20 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobportals', '0003_auto_20220520_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobdetail',
            name='the_amount_of_work_experience',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12'), (13, '13'), (14, '14'), (15, '15'), (16, '16'), (17, '17')]),
        ),
    ]
