# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

CMDPROTOCOL_CHOICES = (
    (0,''),
    (1,'REST API'),
    (2,'SOAP'),
    (3,'Telnet'),
    (4,'TL1'),
    (5,'SSH'),
)
CMDSYSTEM_CHOICES = (
    (0,''),
    (1,'AMS5520'),
    (2,'AXSVision'),
    (3,'Calix'),
    (4,'JunOS'),
    (5,'JunOSe'),
)

class Cmds(models.Model):

    cmdprotocol = models.CharField(max_length=255, choices=CMDPROTOCOL_CHOICES, default=0)
    cmdsystem = models.CharField(max_length=255, choices=CMDSYSTEM_CHOICES, default=0)
    cmdset = models.CharField(max_length=255, default='')
    cmdline = models.CharField(max_length=255, default='\n')
    timestamp = models.DateTimeField(auto_now_add=True)

"""
class CmdSystems(models.Model):
    CMDSYSTEMS_CHOICES = (
        (1,'AMS5520'),
        (2,'AXSVision'),
        (3,'Calix'),
        (4,'JunOS'),
        (5,'JunOSe'),
        (6,'Triad'),
    )
    cmdprotocolkey = models.ForeignKey('CmdProtocols', on_delete=models.CASCADE)
    cmdsystem = models.CharField(max_length=255, choices=CMDSYSTEMS_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

class CmdSets(models.Model):
    cmdsystemkey = models.ForeignKey('CmdSystems', on_delete=models.CASCADE)
    cmdset = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)

class Cmds(models.Model):
    cmdsetkey = models.ForeignKey('CmdSystems', on_delete=models.CASCADE)
    cmdset = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
"""
