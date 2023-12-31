# Generated by Django 3.2.19 on 2023-06-21 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(editable=False, max_length=32)),
                ('full_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=65)),
                ('phone_number', models.CharField(max_length=20)),
                ('date_now', models.DateTimeField(auto_now_add=True)),
                ('order_total', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0)),
                ('lineitem_total', models.DecimalField(decimal_places=2, editable=False, max_digits=6)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.events')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventitems', to='checkout.order')),
            ],
        ),
    ]
