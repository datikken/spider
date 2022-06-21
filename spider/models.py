from django.db import models

class LinkToCrawl(models.Model):
    def __str__(self):
        return self.url

    url = models.CharField(max_length=255)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)