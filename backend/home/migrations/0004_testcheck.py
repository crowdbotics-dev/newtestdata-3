# Generated by Django 2.2.26 on 2022-02-23 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_testnews'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testcheck',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('testapps', models.URLField()),
                ('oktestnew', models.TextField()),
            ],
        ),
    ]
