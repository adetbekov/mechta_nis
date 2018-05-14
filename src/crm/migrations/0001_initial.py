# Generated by Django 2.0.5 on 2018-05-13 04:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('iin', models.CharField(max_length=12)),
                ('last_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('father_name', models.CharField(max_length=20)),
                ('date_in', models.DateTimeField(default=datetime.datetime(2018, 5, 13, 10, 17, 27, 841521))),
                ('date_out', models.DateTimeField(null=True)),
                ('payment_form', models.CharField(choices=[('O', 'Другое'), ('M', 'MasterCard'), ('C', 'Наличный расчет'), ('V', 'Visa')], default='O', max_length=1)),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
    ]
