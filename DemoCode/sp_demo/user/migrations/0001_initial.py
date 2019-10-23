# Generated by Django 2.1.7 on 2019-09-29 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True)),
                ('phone', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=128)),
                ('email', models.CharField(max_length=128)),
                ('avatar', models.CharField(max_length=512)),
                ('ctime', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]