# Generated by Django 3.1.7 on 2021-06-19 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pizza_type', models.CharField(choices=[('Regular', 'Regular Pizza'), ('Square', 'Square Pizza')], max_length=100)),
                ('pizza_size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')], max_length=100)),
            ],
        ),
    ]