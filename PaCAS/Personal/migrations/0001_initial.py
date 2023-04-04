# Generated by Django 4.2 on 2023-04-03 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ObjWorks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, verbose_name='Имя')),
                ('is_taskmaster', models.BooleanField(default=False, null=True, verbose_name='Начальник участка')),
                ('is_master', models.BooleanField(default=False, null=True, verbose_name='Мастер')),
            ],
            options={
                'verbose_name': 'Персонал',
                'verbose_name_plural': 'Персонал',
            },
        ),
        migrations.CreateModel(
            name='Brigade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brigade_id', models.PositiveIntegerField(verbose_name='ID рабочей команды')),
                ('workers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Personal.personal', verbose_name='Закрепленные работники')),
            ],
            options={
                'verbose_name': 'Бригада',
                'verbose_name_plural': 'Бригады',
            },
        ),
    ]
