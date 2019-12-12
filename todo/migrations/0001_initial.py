# Generated by Django 2.2.7 on 2019-11-05 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100)),
                ('done', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
    ]