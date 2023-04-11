# Generated by Django 4.2 on 2023-04-11 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sector', models.CharField(max_length=255)),
                ('nav', models.DecimalField(decimal_places=10, max_digits=20)),
                ('dividend', models.DecimalField(decimal_places=2, max_digits=10)),
                ('first_quarter', models.DecimalField(decimal_places=2, max_digits=15)),
                ('second_quarter', models.DecimalField(decimal_places=2, max_digits=15)),
                ('third_quarter', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('official_news', models.TextField()),
                ('date', models.DateField()),
                ('directors_share_buy', models.DecimalField(decimal_places=2, max_digits=15)),
                ('directors_share_sell', models.DecimalField(decimal_places=2, max_digits=15)),
            ],
        ),
        migrations.CreateModel(
            name='TradingStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('share_price', models.DecimalField(decimal_places=2, max_digits=15)),
                ('volume', models.IntegerField()),
                ('total_trades', models.IntegerField()),
                ('stock', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock_simulator.company')),
            ],
        ),
    ]