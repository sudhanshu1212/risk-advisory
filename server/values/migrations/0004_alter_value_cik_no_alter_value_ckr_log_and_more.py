# Generated by Django 4.1.1 on 2022-09-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0003_alter_value_cik_no_alter_value_cusip_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='cik_no',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='value',
            name='ckr_log',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='value',
            name='company_name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='value',
            name='currency_id',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='value',
            name='cusip',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='value',
            name='data_source_id',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='value',
            name='employees_count',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='value',
            name='exchange_id',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='value',
            name='id',
            field=models.CharField(max_length=6, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='value',
            name='image_aspect_ratio',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='value',
            name='image_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='value',
            name='is_Active',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='value',
            name='phone_no',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='value',
            name='sic_no',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='value',
            name='similar_fund_log',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='value',
            name='url_slug',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='value',
            name='website',
            field=models.CharField(max_length=30),
        ),
    ]
