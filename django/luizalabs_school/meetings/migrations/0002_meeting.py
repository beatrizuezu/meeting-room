# Generated by Django 2.1 on 2018-09-23 00:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
                ('start_at', models.DateTimeField(verbose_name='start_at')),
                ('end_at', models.DateTimeField(verbose_name='end_at')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='meetings.Room')),
            ],
        ),
    ]