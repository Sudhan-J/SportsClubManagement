# Generated by Django 4.0 on 2022-05-27 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Br_name', models.CharField(max_length=30)),
                ('Br_manager', models.CharField(max_length=20)),
                ('Br_location', models.CharField(max_length=30)),
                ('Br_phone', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E_name', models.CharField(max_length=30)),
                ('E_teams', models.CharField(default=None, max_length=30)),
                ('E_date', models.DateField()),
                ('E_time', models.TimeField()),
                ('E_location', models.CharField(max_length=30)),
                ('E_price', models.IntegerField()),
                ('E_seat', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='EventReg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=30)),
                ('Salary', models.IntegerField()),
                ('MailID', models.EmailField(max_length=254)),
                ('Phone', models.BigIntegerField()),
                ('Department', models.TextField()),
                ('Designation', models.CharField(max_length=30)),
                ('ATTEND', models.ManyToManyField(to='psite.Event')),
                ('Br', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psite.branch')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('C_name', models.CharField(max_length=20)),
                ('C_phone', models.BigIntegerField()),
                ('C_address', models.TextField()),
                ('C_mail', models.EmailField(max_length=254)),
                ('C_password', models.CharField(max_length=200)),
                ('BOOK', models.ManyToManyField(to='psite.Event')),
            ],
        ),
        migrations.CreateModel(
            name='BOOK',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('T_date', models.DateField()),
                ('No_seats', models.IntegerField(default=None)),
                ('Cust', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psite.customer')),
                ('EV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psite.event')),
            ],
        ),
        migrations.CreateModel(
            name='ATTEND',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('E', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psite.employee')),
                ('EV', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='psite.event')),
            ],
        ),
    ]
