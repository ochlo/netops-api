# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-09 06:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CmdProtocols',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmdprotocol', models.CharField(choices=[(1, 'REST API'), (2, 'SOAP'), (3, 'Telnet'), (4, 'TL1'), (5, 'SSH')], max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Cmds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmdset', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CmdSets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmdset', models.CharField(max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='CmdSystems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmdprotocol', models.CharField(choices=[(1, 'AMS5520'), (2, 'AXSVision'), (3, 'Calix'), (4, 'JunOS'), (5, 'JunOSe'), (6, 'Triad')], max_length=255)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('cmdprotocolkey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.CmdProtocols')),
            ],
        ),
        migrations.AddField(
            model_name='cmdsets',
            name='cmdsystemkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.CmdSystems'),
        ),
        migrations.AddField(
            model_name='cmds',
            name='cmdsetkey',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ops.CmdSystems'),
        ),
    ]