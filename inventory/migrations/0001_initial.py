# Generated by Django 4.2.5 on 2023-09-06 00:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ref_code', models.CharField(max_length=10)),
                ('category', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('discount', models.IntegerField(max_length=2)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
