from django.db import models


class LingLogManager(models.Manager):

    def create_from_request(self, link, request):
        linklog = self.model(
            link=link,
            http_accept_language=request.META.get("HTTP_ACCEPT_LANGUAGE", ""),
            http_host=request.META.get("HTTP_HOST", ""),
            http_referer=request.META.get("HTTP_REFERER", ""),
            http_user_agent=request.META.get("HTTP_USER_AGENT", ""),
            query_string=request.META.get("QUERY_STRING", ""),
            remote_addr=request.META.get("REMOTE_ADDR", ""),
            remote_host=request.META.get("REMOTE_HOST", ""),
            request_method=request.META.get("REQUEST_METHOD", ""),
        )
        linklog.save()
        return linklog
