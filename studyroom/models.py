from django.db import models
from django.core.validators import (
    MaxValueValidator,
)

SECTION_OPTIONS = (
    ('GA', 'General Ability'),
    ('MATH', 'Mathematics'),
    ('none', 'None')
)

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=60, blank=False)
    slug = models.SlugField(max_length=60, blank=False, help_text="a user friendly url")
    # random_order = models.BooleanField(blank=False, default=False, verbose_name="Random Order", help_text="Display the questions in a random order or as they are set?")
    # max_question = models.PositiveIntegerField(blank=True, null=True, verbose_name="Max Questions", help_text="Number of questions to be answered on each attempt.")
    # answers_at_end
    # pass_mark = models.SmallIntegerField(blank=True, default=0, verbose_name="Pass Mark", help_text="Percentage required to pass exam.", validators=[MaxValueValidator(100)])
    
    def __str__(self):
        return self.title
    
class Question(models.Model):
    quiz = models.ForeignKey(Quiz,verbose_name="Quiz", blank=True, on_delete=models.CASCADE)
    text = models.CharField(max_length=150, blank=False)
    section = models.CharField(max_length=30, null=True, blank=True, choices=SECTION_OPTIONS)

    def __str__(self):
        return self.text

class Answer(models.Model):
    content = models.CharField(max_length=200, blank=False, help_text="Enter the answer text that you want to displayed", verbose_name="Content")
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    active = models.BooleanField(blank=False, default=True, help_text="is this a active answer?", verbose_name="Active")
    correct = models.BooleanField(blank=False, default=False, help_text="Is this a correct answer?", verbose_name="Correct")

    def __str__(self):
        return self.content