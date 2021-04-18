# Generated by Django 3.2 on 2021-04-18 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectConfig',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=255)),
                ('company_email', models.CharField(max_length=255)),
                ('company_phone', models.CharField(max_length=100)),
                ('company_address', models.CharField(max_length=255)),
                ('company_fax', models.IntegerField(default=0)),
                ('company_logo', models.ImageField(upload_to='logo')),
            ],
        ),
    ]
