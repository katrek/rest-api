from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=100, blank=False, verbose_name='Blog title')
    text = models.TextField(verbose_name='Text')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', related_name='posts', on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.title

