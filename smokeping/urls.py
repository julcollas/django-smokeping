from django.conf.urls import patterns

urlpatterns = patterns('',
    (r'^targets$', 'smokeping.views.targets'),
    (r'^alerts$', 'smokeping.views.alerts'),
    (r'^parents$', 'smokeping.views.parents'),
    (r'^slaves$', 'smokeping.views.slaves'),
    (r'^probes$', 'smokeping.views.probes'),
    (r'^export$', 'smokeping.views.export'),
    (r'^secrets$', 'smokeping.views.secrets'),
)
