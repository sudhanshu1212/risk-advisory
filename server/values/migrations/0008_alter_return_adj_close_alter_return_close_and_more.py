# Generated by Django 4.1.1 on 2022-09-16 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('values', '0007_alter_return_adj_close_alter_return_close_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='return',
            name='adj_close',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='return',
            name='close',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='return',
            name='high',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='return',
            name='low',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='return',
            name='open',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
        migrations.AlterField(
            model_name='return',
            name='returns',
            field=models.DecimalField(decimal_places=10, max_digits=19),
        ),
    ]