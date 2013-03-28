from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _


class Slave(models.Model):
    name = models.CharField(max_length=20, unique=True)
    color = models.CharField(max_length=6, default='0000ff')
    location = models.CharField(max_length=100)
    secret = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.name)
    

class Probe(MPTTModel):
    name = models.CharField(max_length=100)
    port = models.BooleanField()
    option = models.TextField(null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return u'%s' % (self.name)
    

class Parent(models.Model):
    name = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100)

    def __unicode__(self):
        return u'%s' % (self.title)

    
class Chart(MPTTModel):
    name = models.CharField(max_length=100)
    menu = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    slave = models.ForeignKey(Slave, null=True, blank=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __unicode__(self):
        return u'%s' % (self.menu)

    
class Alert(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=100, unique=False)
    to = models.EmailField()
    mailtemplate = models.CharField(max_length=100)
    comment = models.CharField(max_length=100)
    pattern = models.CharField(max_length=100, unique=False)
    edgetrigger = models.CharField(max_length=100, default='yes')

    def __unicode__(self):
        return u'%s' % (self.name)


class Target(models.Model):
    menu = models.CharField(max_length=100)
    title = models.CharField(max_length=200, help_text="Menu (Ip) - Probe [Port]")
    name = models.CharField(max_length=100, help_text="[-_0-9a-zA-Z] Example: 192-168-0-1-22")
    host = models.CharField(max_length=50, help_text="IP or hostname")
    probe = TreeForeignKey(Probe, null=True, blank=False)
    port = models.IntegerField(null=True, blank=True, default=None)
    chart = TreeForeignKey(Chart, null=True, blank=False, help_text="Implicitly defines the slave.")
    alert = models.ManyToManyField(Alert, default=None, blank=True, null=True)
    parent = models.ManyToManyField(Parent, default=None, blank=True, null=True)
    parent_tag = models.CharField(max_length=20, default=None, blank=True, null=True)
    nomasterpoll = models.BooleanField(default=False, help_text="Use this in a master/slave setup where the master must not poll a particular target.")

    def clean(self):
        """
        Validate custom constraints (port / probe)
        """
        if self.probe:
            if self.probe.port is True and self.port is None:
                raise ValidationError(_(u"Probe %s need a port!" % self.probe.name))
            if self.probe.port is False and self.port is not None:
                raise ValidationError(_(u"Probe %s don't need a port!" % self.probe.name))

    class Meta:
        """
        Set the couple name & chart as unique
        """
        unique_together = ('name', 'chart',)

    def get_alert(self):
        """
        Return a list of all selected alerts as string if any
        """
        ret_val = ', '.join([val['name'] for val in self.alert.values()])
        return ret_val
    get_alert.short_description = 'Alert'

    def get_parent(self):
        """
        Return a list of all selected parent as string if any
        """
        ret_val = ', '.join([val['name'] for val in self.parent.values()])
        return ret_val
    get_parent.short_description = 'Parent'

    def __unicode__(self):
        return u'%s:%s %s' % (self.host, str(self.port), self.chart)


