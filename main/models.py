from django.db import models
from django.utils import timezone
from django.urls import reverse


# Таблица с данными трафика
class Data(models.Model):
    action_time = models.DateTimeField(default=timezone.now)
    ethernet_dst = models.TextField()
    ethernet_src = models.TextField()
    ip_proto = models.TextField()
    ip_dst = models.TextField()
    ip_src = models.TextField()
    tcp_sport = models.TextField()
    tcp_dport = models.TextField()
    raw = models.TextField()

    class Meta:
        db_table = 'data_set'

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)


# Тип протоколов
PROTOCOL_CHOICES = (
    ('6','TCP'),
    ('17', 'UDP'),
    ('1','ICMP'),
)


# Таблица с сигнатурами
class Signature(models.Model):
    name = models.CharField('Имя сигнатуры', max_length=200)
    ip_proto = models.CharField('Протокол (По умолчанию ANY)', max_length=6, choices=PROTOCOL_CHOICES, default=None, blank=True)
    ip_src = models.GenericIPAddressField('IP адрес источника (По умолчанию ANY)', default='', blank=True,  null=True)
    ip_dst = models.GenericIPAddressField('IP адрес назначения (По умолчанию ANY)', default='', blank=True,  null=True)
    ip_sport = models.CharField('Порт источника (По умолчанию ANY)', max_length=6, default=None, blank=True)
    ip_dport = models.CharField('Порт назначения (По умолчанию ANY)', max_length=6, default=None, blank=True)
    raw = models.TextField('Сигнатура', default=None)

    class Meta:
        db_table = 'signature'

    def __str__(self):
        return str(self.name)

    def __unicode__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse('main:all_signature')


# Таблица для вывода сигнатур по которым есть срабатывания
class Alerts(models.Model):
    signature_name = models.CharField(max_length=200)
    id_signature = models.TextField()
    action_time = models.DateTimeField()
    ethernet_dst = models.TextField()
    ethernet_src = models.TextField()
    ip_proto = models.TextField()
    ip_dst = models.TextField()
    ip_src = models.TextField()
    tcp_sport = models.TextField()
    tcp_dport = models.TextField()
    raw = models.TextField()

    class Meta:
        db_table = 'alerts_set'

    def __str__(self):
        return str(self.id)

    def __unicode__(self):
        return str(self.id)
