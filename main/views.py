from .models import Signature, Data, Alerts
from django.views import View, generic
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from django.db.models import Q


# Вывод данных из из модели Signature
class Post_list(generic.ListView):
    template_name = 'main/signature.html'
    context_object_name = 'all_signature'

    def get_queryset(self):
        return Signature.objects.all()


# Получение данных по сигнатурам из собраного трафика
class Alert(generic.ListView):
    # Очишаем таблицу
    Alerts.objects.all().delete()
    # Проверяем каждую сигнатуру по очереди
    for i in Signature.objects.all():
        # Проверяем параметры для поиска
        data_ip_src = False if i.ip_src == None else True
        data_ip_dst = False if i.ip_dst == None else True
        data_ip_sport = False if i.ip_sport == '' else True
        data_ip_dport = False if i.ip_dport == '' else True
        data_ip_proto = False if i.ip_proto == '' else True

        # Делаем запрос к нашей таблици с трафиклм
        query = Data.objects.filter((Q(ip_src=i.ip_src) | Q(ip_src__isnull=data_ip_src))
                                    & (Q(ip_dst=i.ip_dst) | Q(ip_dst__isnull=data_ip_dst))
                                    & (Q(tcp_sport=i.ip_sport) | Q(tcp_sport__isnull=data_ip_sport))
                                    & (Q(tcp_dport=i.ip_dport) | Q(tcp_dport__isnull=data_ip_dport))
                                    & (Q(ip_proto=i.ip_proto) | Q(ip_proto__isnull=data_ip_proto))
                                    & Q(raw__icontains=i.raw))
        # Каждый результат записываем в таблицу для вывода
        for m in query.values_list():
            alert = Alerts.objects.create(signature_name=i.name,
                                          id_signature=m[0],
                                          action_time=m[1],
                                          ethernet_dst=m[2],
                                          ethernet_src=m[3],
                                          ip_proto=m[4],
                                          ip_dst=m[5],
                                          ip_src=m[6],
                                          tcp_sport=m[7],
                                          tcp_dport=m[8],
                                          raw=m[9])
    # Имя шаблона для вывода
    template_name = 'main/index.html'
    context_object_name = 'all_alerts'

    # Вывод всех полученных срабатываний
    def get_queryset(self):
        return Alerts.objects.all()


# Представление для создания сигнатуры
class Create_signature(CreateView):
    model = Signature
    fields = ['name', 'ip_proto', 'ip_src', 'ip_dst', 'ip_sport', 'ip_dport', 'raw']


# Представление для изменения сигнатуры
class Update_signature(UpdateView):
    model = Signature
    fields = ['name', 'ip_proto', 'ip_src', 'ip_dst', 'ip_sport', 'ip_dport', 'raw']


# Представление для удлаения сигнатуры
class Delete_signature(DeleteView):
    model = Signature
    success_url = reverse_lazy('main:all_signature')