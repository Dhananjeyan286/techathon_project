# Generated by Django 3.2.8 on 2021-11-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('email_id', models.CharField(max_length=55, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=55)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]