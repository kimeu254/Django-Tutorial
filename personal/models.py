from django.db import models

PRIORITY_CHOICES = (
    ('l', 'Low'),
    ('m', 'Medium'),
    ('h', 'High'),
)

class Question(models.Model):
    title = models.CharField(max_length=100)
    question = models.TextField(max_length=400)
    priority = models.CharField(max_length=1, choices=PRIORITY_CHOICES)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'A Question'
        verbose_name_plural = "Peoples's Questions"

