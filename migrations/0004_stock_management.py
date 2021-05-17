# Generated by Django 3.2 on 2021-05-13 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('GUE_Admin123', '0003_auto_20210513_2116'),
    ]

    operations = [
        migrations.CreateModel(
            name='stock_management',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stock', models.CharField(max_length=100)),
                ('prodid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='GUE_Admin123.pdt_reg_tbl')),
            ],
        ),
    ]
