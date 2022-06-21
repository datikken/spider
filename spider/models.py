from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey


class LinkToCrawl(models.Model):
    def __str__(self):
        return self.url

    url = models.CharField(max_length=255)
    status = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class CrawledLink(models.Model):
    def __str__(self):
        return self.url

    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    link_to_crawl = models.ForeignKey(LinkToCrawl, default=None, on_delete=models.CASCADE)


