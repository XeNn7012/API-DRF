# Generated by Django 4.0.2 on 2022-02-26 12:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='People_Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('company_name', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('zip', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('web', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
            ],
        ),
    ]