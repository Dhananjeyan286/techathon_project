# Generated by Django 3.2.8 on 2021-11-19 02:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_react', '0002_auto_20211118_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email_id',
            field=models.EmailField(max_length=55, primary_key=True, serialize=False),
        ),
    ]
