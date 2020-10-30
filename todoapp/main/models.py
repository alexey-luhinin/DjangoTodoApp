from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField('Заголовок', max_length=200)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Список дел'
        verbose_name_plural = 'Список дел'
