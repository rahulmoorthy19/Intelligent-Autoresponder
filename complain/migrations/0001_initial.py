# Generated by Django 2.1.4 on 2018-12-25 10:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='query',
            fields=[
                ('query_id', models.AutoField(primary_key=True, serialize=False)),
                ('email_id', models.EmailField(max_length=75)),
                ('query_ques', models.TextField()),
                ('answer', models.TextField(blank=True)),
                ('query_type', models.IntegerField(default=0)),
                ('sys_conf', models.IntegerField(default=1)),
                ('answered_flag', models.IntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='team',
            fields=[
                ('team_id', models.AutoField(primary_key=True, serialize=False)),
                ('team_name', models.CharField(max_length=10)),
                ('team_type', models.CharField(max_length=10)),
                ('team_email_id', models.EmailField(max_length=75)),
                ('workload', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Username',
            fields=[
                ('name', models.CharField(max_length=10)),
                ('phone_no', models.CharField(max_length=12)),
                ('email_id', models.EmailField(max_length=75, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='query',
            name='team_assigned_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='complain.team'),
        ),
    ]
