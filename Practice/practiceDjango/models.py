from django.db import models


class Task(models.Model):
    content     = models.TextField()
    created_at  = models.DateTimeField(auto_now=True)
    deadline    = models.DateTimeField()
    done        = models.BooleanField(default=False)
    tags        = models.ManyToManyField('Tag', related_name='tasks')

    class Meta:
        ordering = ['done', '-created_at']

    def __str__(self):
        return self.content


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
