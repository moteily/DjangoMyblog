# Generated by Django 3.0.3 on 2020-09-02 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataShow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='system_monit_cpu',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('cpu_cores', models.IntegerField()),
                ('cur_cpu', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cur_mem', models.IntegerField()),
                ('mem_rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('mem_all', models.IntegerField()),
                ('create_time', models.DateTimeField()),
                ('time_stamp', models.BigIntegerField()),
            ],
        ),
    ]
