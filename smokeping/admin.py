# -*- coding: utf-8 -*-
from django.contrib import admin
from django.forms import TextInput, Textarea
from django.db import models
from mptt.admin import MPTTModelAdmin
from smokeping.models import Target
from smokeping.models import Chart
from smokeping.models import Slave
from smokeping.models import Probe
from smokeping.models import Parent
from smokeping.models import Alert


class TargetAdmin(admin.ModelAdmin):
    '''
    TargetAdmmin Class with display, filter and search settings
    '''
    list_display = ['menu', 'host', 'probe', 'port', 'chart', 'parent_tag', 'get_alert', 'get_parent']
    list_filter = ['probe', 'chart']
    search_fields = ['host', 'port', 'menu']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
    }


class AlertAdmin(admin.ModelAdmin):
    '''
    AlertAdmmin Class with display and filter settings
    '''
    list_display = ['name', 'pattern', 'type']
    list_filter = ['type']

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'50'})},
    }


class ChartAdmin(MPTTModelAdmin):
    '''
    ChartAdmmin Class with display and filter settings
    '''
    list_display = ['name', 'slave']
    list_filter = ['slave']


class ProbeAdmin(MPTTModelAdmin):
    '''
    ProbeAdmmin Class with display settings
    '''
    list_display = ['name', 'port']


class SlaveAdmin(admin.ModelAdmin):
    '''
    ProbeAdmmin Class with display settings
    '''
    list_display = ['name', 'location']


admin.site.register(Parent)
admin.site.register(Target, TargetAdmin)
admin.site.register(Slave, SlaveAdmin)
admin.site.register(Probe, ProbeAdmin)
admin.site.register(Alert, AlertAdmin)
admin.site.register(Chart, ChartAdmin)