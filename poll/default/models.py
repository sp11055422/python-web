from django.db import models


# 使用符合 Django 慣例的 Model 命名 (大寫首字母)
class Poll(models.Model):
    subject = models.CharField("投票主題", max_length=64)
    desc = models.TextField("說明", blank=True)
    created = models.DateField("建立日期", auto_now_add=True)

    class Meta:
        verbose_name = "投票主題"
        verbose_name_plural = "投票主題"

    def __str__(self):
        return self.subject


class Option(models.Model):
    title = models.CharField("選項文字", max_length=64)
    votes = models.IntegerField("票數", default=0)
    # 使用 ForeignKey 取代原本的 poll_id 整數欄位
    poll = models.ForeignKey(Poll, related_name='options', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "選項"
        verbose_name_plural = "選項"

    def __str__(self):
        return f"{self.poll_id if hasattr(self,'poll_id') else self.poll.id} - {self.title} : {self.votes}"

