# Generated by Django 2.1.3 on 2018-11-28 08:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('trouble', models.BooleanField()),
                ('oversea', models.BooleanField()),
                ('status', models.CharField(max_length=50)),
                ('company', models.CharField(max_length=200)),
                ('customer', models.CharField(max_length=50)),
                ('Tel', models.CharField(max_length=50)),
                ('robot', models.CharField(max_length=200)),
                ('controller', models.CharField(max_length=200)),
                ('no_name', models.CharField(max_length=50)),
                ('option', models.CharField(max_length=50)),
                ('inquiry', models.TextField()),
                ('answer', models.TextField()),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]