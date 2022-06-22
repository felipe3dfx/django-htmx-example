from django.db import models


class Card(models.Model):
    title = models.CharField(max_length=128, unique=True)

    image = models.ImageField()

    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ['-id']
        verbose_name = 'card'
        verbose_name_plural = 'cards'
