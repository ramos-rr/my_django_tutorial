import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    total_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.question_text

    @admin.display(
        ordering='question.id',
        description='ID'
    )
    def get_id(self):
        return self.id

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?',
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Future Question?',
    )
    def future_question(self):
        now = timezone.now()
        return True if self.pub_date > now else False

    @admin.display(
        ordering='total_votes',
        description='Global votes',
    )
    def get_total_votes(self):
        s = 0
        for choice in self.choice_set.all():
            s += choice.votes
        self.total_votes = s
        return self.total_votes


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
