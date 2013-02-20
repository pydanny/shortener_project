from django.contrib import admin

from .models import LinkLog

class LinkLogAdmin(admin.ModelAdmin):
    
    readonly_fields = (
        "link", 
        "http_accept_language",
        "http_host",
        "http_referer",
        "http_user_agent",
        "query_string",
        "remote_addr",
        "remote_host",
        "request_method"
    )

admin.site.register(LinkLog, LinkLogAdmin)
