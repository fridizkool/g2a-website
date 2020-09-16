# Generated by Django 2.2.16 on 2020-09-15 23:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Un-named', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('policy_type', models.CharField(max_length=40)),
                ('expiration', models.DateField(verbose_name='Expiration Date')),
                ('section', models.CharField(max_length=12)),
                ('language', models.TextField()),
                ('category', models.CharField(max_length=40)),
                ('impact', models.CharField(max_length=256)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Location')),
            ],
        ),
    ]
