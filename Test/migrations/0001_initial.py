# Generated by Django 3.0.4 on 2020-05-03 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a1', models.CharField(choices=[('0', 'Po'), ('1', 'Jo')], default=None, max_length=128)),
                ('a2', models.CharField(choices=[('0', 'Po'), ('1', 'Jo')], default=None, max_length=128)),
                ('a3', models.CharField(choices=[('0', 'Po'), ('1', 'Jo')], default=None, max_length=128)),
                ('a4', models.CharField(choices=[('0', 'Po'), ('1', 'Jo')], default=None, max_length=128)),
                ('a5', models.CharField(choices=[('0', 'Po'), ('1', 'Jo')], default=None, max_length=128)),
                ('a6', models.CharField(choices=[('0', 'Po'), ('1', 'Jo')], default=None, max_length=128)),
                ('a7', models.CharField(choices=[('0', 'Po'), ('1', 'Jo')], default=None, max_length=128)),
                ('a8', models.CharField(choices=[('0', 'Po'), ('1', 'Jo')], default=None, max_length=128)),
                ('a9', models.CharField(choices=[('0', 'Po'), ('1', 'Jo')], default=None, max_length=128)),
                ('a10', models.CharField(choices=[('0', 'Po'), ('1', 'Jo')], default=None, max_length=128)),
                ('gjinia', models.CharField(choices=[('1', 'Mashkull'), ('0', 'Femer')], default=None, max_length=128)),
                ('mosha_ne_muaj', models.CharField(default=None, max_length=3)),
                ('etnia', models.IntegerField(default=5)),
                ('verdheza', models.CharField(choices=[('1', 'Po'), ('0', 'Jo')], default=None, max_length=128)),
                ('family', models.CharField(choices=[('1', 'Po'), ('0', 'Jo')], default=None, max_length=128)),
            ],
        ),
    ]
