# Generated by Django 3.0.7 on 2020-07-03 23:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfinance', '0004_category_budget'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='parent_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myfinance.Category'),
        ),
        migrations.AlterField(
            model_name='category',
            name='budget',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='myfinance.Budget'),
        ),
    ]
