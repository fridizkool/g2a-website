# Generated by Django 3.1.3 on 2021-09-21 15:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PxPUC', '0003_glossaryterm'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchQuery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query', models.TextField()),
                ('timestamp', models.DateTimeField()),
                ('results', models.IntegerField()),
            ],
        ),
    ]
