# -*- coding: utf-8 -*-

# Create your views here.

from django.http import HttpResponse
from django.template import Context, loader
from django.utils import simplejson
from smokeping.models import Target
from smokeping.models import Chart
from smokeping.models import Alert
from smokeping.models import Parent
from smokeping.models import Slave
from smokeping.models import Probe

def targets(request):
    target_list = Target.objects.all()
    chart_list = Chart.objects.all()
    t = loader.get_template('smokeping/targets.html')
    c = Context({
        'target_list': target_list,
        'chart_list': chart_list,
    })
    return HttpResponse(t.render(c), mimetype='text/plain')


def alerts(request):
    alert_list = Alert.objects.all()
    t = loader.get_template('smokeping/alerts.html')
    c = Context({
        'alert_list': alert_list,
    })
    return HttpResponse(t.render(c), mimetype='text/plain')


def parents(request):
    parent_list = Parent.objects.all()
    t = loader.get_template('smokeping/parents.html')
    c = Context({
        'parent_list': parent_list,
    })
    return HttpResponse(t.render(c), mimetype='text/plain')


def slaves(request):
    slave_list = Slave.objects.all()
    t = loader.get_template('smokeping/slaves.html')
    c = Context({
        'slave_list': slave_list,
    })
    return HttpResponse(t.render(c), mimetype='text/plain')


def probes(request):
    probe_list = Probe.objects.all()
    t = loader.get_template('smokeping/probes.html')
    c = Context({
        'probe_list': probe_list,
    })
    return HttpResponse(t.render(c), mimetype='text/plain')


def export(request):
    target_list = Target.objects.all()
    dict = {}
    for target in target_list:
        if target.host not in dict:
            dict[target.host] = []
        chart_ancestors = target.chart.get_ancestors(include_self=True)
        chart_ancestors = '.'.join([c.name for c in chart_ancestors])
        url = chart_ancestors + '.' + target.name
        t_dict = {'name': target.name,
                  'title': target.title,
                  'slave': target.chart.slave.name,
                  'chart': target.chart.menu,
                  'menu': target.menu,
                  'probe': target.probe.name,
                  'port': target.port,
                  'url': url} 

        dict[target.host].append(t_dict)
        
    json = simplejson.dumps(dict, indent=4)
    return HttpResponse(json, mimetype='application/json')


def secrets(request):
    slave_list = Slave.objects.all()
    t = loader.get_template('smokeping/secrets.html')
    c = Context({
        'slave_list': slave_list,
    })
    return HttpResponse(t.render(c), mimetype='text/plain')



