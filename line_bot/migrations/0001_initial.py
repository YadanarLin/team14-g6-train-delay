# Generated by Django 3.2.9 on 2021-12-22 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LocalStorage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_update', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrainInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_id', models.CharField(max_length=200)),
                ('railway_en', models.CharField(default='undefined', max_length=200)),
                ('railway_ja', models.CharField(default='undefined', max_length=200)),
                ('operator_en', models.CharField(default='undefined', max_length=200)),
                ('operator_ja', models.CharField(default='undefined', max_length=200)),
                ('information_ja', models.CharField(max_length=2000)),
                ('information_en', models.CharField(max_length=2000)),
            ],
        ),
    ]

