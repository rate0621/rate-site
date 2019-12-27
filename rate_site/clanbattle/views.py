from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, UpdateView

from clanbattle.models import *
from clanbattle.forms import BossForm, AttackLogForm

from datetime import datetime
from dateutil.relativedelta import relativedelta

def get_past_month(target, current, selected_month):
    arr = []

    while 1:
        choise = ''
        if target.strftime("%Y-%m-%d") == selected_month:
            choise = True
        else:
            choise = False

        arr.append((target.year, target.month, choise))
        target = target + relativedelta(months=1)

        if target > current:
            break


    return arr


class CbListView(TemplateView):
    template_name = "clanbattle/cb_list.html"

    def get(self, request, *args, **kwargs):
        context = super(CbListView, self).get_context_data(**kwargs)

        boss = Boss.objects.all()  # データベースからオブジェクトを取得して
        context['boss'] = boss  # 入れ物に入れる

        current_boss = CurrentBoss.objects.all()  # データベースからオブジェクトを取得して
        context['current_boss'] = current_boss  # 入れ物に入れる

        selected_month = request.GET.get("month")
        context['selected_month'] = selected_month

        if selected_month is None:
            target = datetime.today()
            f      = datetime.strftime(target, '%Y-%m-01')
            t      = datetime.strftime(target + relativedelta(months=1), '%Y-%m-01')
        else:
            f      = datetime.strftime(datetime.strptime(selected_month, '%Y-%m-%d'), '%Y-%m-01')
            t      = datetime.strftime(datetime.strptime(selected_month, '%Y-%m-%d') + relativedelta(months=1), '%Y-%m-01')
            


        a_log = AttackLog.objects.filter(attack_time__range=(f, t)).order_by('attack_time').reverse()[:20]  # データベースからオブジェクトを取得して
        context['a_log'] = a_log  # 入れ物に入れる

        # クラバトのデータを取り始めたのが2019/09から
        context['past_month'] = get_past_month(datetime.strptime('2019-09-01', '%Y-%m-%d'), datetime.strptime(datetime.strftime(datetime.today(), "%Y-%m-01"), '%Y-%m-%d'), selected_month)

        return render(self.request, self.template_name, context)


class BossUpdateView(UpdateView):
    model = Boss
    form_class = BossForm
    success_url = "/clanbattle"

class DamageUpdateView(UpdateView):
    model = AttackLog
    form_class = AttackLogForm
    success_url = "/clanbattle"


#def update(request, boss_number):
#    b1 = get_object_or_404(Boss, pk=boss_number)
#
#    #b1 = Boss.objects.get(boss_number=boss_number)
#    #b = BossForm(request.POST, instance=b1)
#    #b.save()
#    return HttpResponseRedirect(reverse('clanbattle:index'))
