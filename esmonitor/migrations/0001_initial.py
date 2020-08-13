# Generated by Django 3.1 on 2020-08-13 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClusterHost',
            fields=[
                ('name', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('host', models.CharField(max_length=100)),
                ('port', models.IntegerField(default=9200)),
                ('protocol', models.CharField(default='http', max_length=20)),
                ('username', models.CharField(blank=True, max_length=100, null=True)),
                ('password', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Cluster Host',
                'verbose_name_plural': 'Cluster Hosts',
            },
        ),
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('key', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('value', models.TextField()),
            ],
            options={
                'verbose_name': 'Settings',
                'verbose_name_plural': 'Settings',
            },
        ),
        migrations.CreateModel(
            name='Stats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('node_stats', 'node_stats'), ('cluster_stats', 'cluster_stats')], max_length=200)),
                ('request_date', models.DateTimeField(auto_now_add=True)),
                ('json_content', models.TextField()),
                ('cluster_host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='esmonitor.clusterhost')),
            ],
            options={
                'verbose_name': 'Stats',
                'verbose_name_plural': 'Stats',
            },
        ),
        migrations.AddIndex(
            model_name='stats',
            index=models.Index(fields=['-request_date'], name='esmonitor_s_request_34f2c5_idx'),
        ),
        migrations.AlterUniqueTogether(
            name='stats',
            unique_together={('cluster_host_id', 'request_date', 'name')},
        ),
    ]
