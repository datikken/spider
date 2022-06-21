from django.contrib import admin
from .models import LinkToCrawl, CrawledLink
from django.utils.translation import ngettext
from django.contrib import messages


@admin.action(description='Crawl selected links')
def make_crawled(self, request, queryset):
    all = queryset.all()
    for link in all:
        print(link.url)
    updated = queryset.update(status=True)
    self.message_user(request, ngettext(
        '%d Link was successfully marked as published.',
        '%d Links were successfully marked as published.',
        updated,
    ) % updated, messages.SUCCESS)


@admin.register(LinkToCrawl)
class LinkToCrawlAdmin(admin.ModelAdmin):
    list_display = ('url', 'status', 'created_at', 'updated_at')
    actions = [make_crawled]


@admin.register(CrawledLink)
class LinkToCrawlAdmin(admin.ModelAdmin):
    list_display = ('url', 'created_at', 'updated_at')
    actions = [make_crawled]