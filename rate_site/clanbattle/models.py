from django.db import models
from django.urls import reverse


# Create your models here.

class Boss(models.Model):
    class Meta:
        db_table = 'boss'

    #event_month   = models.DateField(verbose_name='開催月', max_length=255)
    boss_id   = models.IntegerField(primary_key=True, verbose_name='番号', null=False, default='')
    boss_name     = models.CharField(verbose_name='ボス名', max_length=255)
    max_hit_point = models.IntegerField(verbose_name='HP')
    target        = models.CharField(verbose_name='ダメージ目安', max_length=255)

    def __str__(self):
        ret = self.boss_name
        return ret

    def get_absolute_url(self):
        return reverse("clanbattle:index")

class ClanMembers(models.Model):
    class Meta:
        db_table = 'clan_members'

    member_id   = models.CharField(primary_key=True, verbose_name='メンバーID', max_length=255, null=False, default='')
    member_name = models.CharField(verbose_name='メンバー名', max_length=255)
    is_member   = models.BooleanField(verbose_name='正式メンバー', default=False)


    def __str__(self):
        ret = self.member_name
        return ret

class BossReserve(models.Model):
    class Meta:
        db_table = 'boss_reserve'

    reserved_at = models.DateTimeField(verbose_name='予約日')
    member      = models.ForeignKey(ClanMembers, verbose_name='メンバー', on_delete=models.CASCADE)
    boss        = models.ForeignKey(Boss,        verbose_name='ボス',     on_delete=models.CASCADE)
    is_attack   = models.BooleanField(verbose_name='凸済み',     default=False)
    is_cancel   = models.BooleanField(verbose_name='キャンセル', default=False)


    def __str__(self):
        ret = self.member
        return ret


class AttackLog(models.Model):
    class Meta:
        db_table = 'attack_log'

    attack_time   = models.DateTimeField(verbose_name='凸時間')
    member        = models.ForeignKey(ClanMembers, verbose_name='メンバー', on_delete=models.CASCADE)
    boss          = models.ForeignKey(Boss,        verbose_name='ボス',     on_delete=models.CASCADE)
    loop_count    = models.IntegerField(verbose_name='週', default=1)
    damage        = models.IntegerField(verbose_name='ダメージ')
    score         = models.IntegerField(verbose_name='スコア')
    is_carry_over = models.IntegerField(verbose_name='持ち越し')
    attack_weight = models.FloatField(verbose_name='重み', default=0)

    def __str__(self):
        ret = self.member
        return ret

class CurrentBoss(models.Model):
    class Meta:
        db_table = 'current_boss'

    boss       = models.ForeignKey(Boss, verbose_name='ボス', on_delete=models.CASCADE)
    hit_point  = models.IntegerField(verbose_name='残りHP')
    loop_count = models.IntegerField(verbose_name='週', default=1)

    def __str__(self):
        ret = self.boss
        return ret


class CarryOver(models.Model):
    class Meta:
        db_table = 'carry_over'

    carried_at  = models.DateTimeField(verbose_name='処理日')
    member      = models.ForeignKey(ClanMembers, verbose_name='メンバー', on_delete=models.CASCADE)
    boss        = models.ForeignKey(Boss,        verbose_name='ボス',     on_delete=models.CASCADE)
    time        = models.IntegerField(verbose_name='持ち越し時間')
    is_attack   = models.BooleanField(verbose_name='凸済み', default=False)

    def __str__(self):
        ret = self.member
        return ret
