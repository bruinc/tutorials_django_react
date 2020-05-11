import datetime

from django.db import models
from django.utils import timezone

# models = database layout
# A model is the single, definitive source of truth about your data. It contains the essential fields 
# and behaviors of the data you’re storing. Django follows the DRY Principle. The goal is to define 
# your data model in one place and automatically derive things from it.

# DRY = Don't repeat yourself.
# Every distinct concept and/or piece of data should live in one, and only one, place. Redundancy is 
# bad. Normalization is good.
# The framework, within reason, should deduce as much as possible from as little as possible.

# This includes the migrations - unlike in Ruby On Rails, for example, migrations are entirely derived 
# from your models file, and are essentially a history that Django can roll through to update your 
# database schema to match your current models.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    
    # Adding attributes to was_published recently to change how it's shown in list display
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
