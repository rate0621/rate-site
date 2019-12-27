from django import forms

from .models import Boss, AttackLog

class BossForm(forms.ModelForm):
    class Meta:
        model = Boss
        fields = ("boss_name", "max_hit_point", "target")


class AttackLogForm(forms.ModelForm):
    class Meta:
        model = AttackLog
        fields = ('damage',)

class SearchForm(forms.Form):
    word = forms.CharField(max_length=250)
