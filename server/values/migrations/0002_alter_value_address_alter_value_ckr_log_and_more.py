# Generated by Django 4.1.1 on 2022-09-16 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='value',
            name='address',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='value',
            name='ckr_log',
            field=models.TextField(max_length=5),
        ),
        migrations.AlterField(
            model_name='value',
            name='company_name',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='value',
            name='cumulative_return',
            field=models.DateTimeField(max_length=10),
        ),
        migrations.AlterField(
            model_name='value',
            name='currency_id',
            field=models.TextField(max_length=5),
        ),
        migrations.AlterField(
            model_name='value',
            name='data_source_id',
            field=models.TextField(max_length=5),
        ),
        migrations.AlterField(
            model_name='value',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='value',
            name='exchange_id',
            field=models.TextField(max_length=5),
        ),
        migrations.AlterField(
            model_name='value',
            name='id',
            field=models.TextField(max_length=6, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='value',
            name='image_aspect_ratio',
            field=models.TextField(max_length=10),
        ),
        migrations.AlterField(
            model_name='value',
            name='industry',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='value',
            name='is_Active',
            field=models.TextField(max_length=5),
        ),
        migrations.AlterField(
            model_name='value',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='value',
            name='phone_no',
            field=models.TextField(max_length=15),
        ),
        migrations.AlterField(
            model_name='value',
            name='sector',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='value',
            name='similar_fund_log',
            field=models.TextField(max_length=5),
        ),
        migrations.AlterField(
            model_name='value',
            name='ticker',
            field=models.CharField(max_length=6),
        ),
        migrations.AlterField(
            model_name='value',
            name='url_slug',
            field=models.TextField(max_length=30),
        ),
        migrations.AlterField(
            model_name='value',
            name='website',
            field=models.TextField(max_length=30),
        ),
    ]
