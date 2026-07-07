from django.conf import settings
from django.db import models


class Link(models.Model):
    original_url = models.URLField(max_length=2048)
    short_code = models.CharField(max_length=6, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    clicks_count = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.short_code} -> {self.original_url}"

    @property
    def short_url(self):
        return f"{settings.BASE_URL}/{self.short_code}"


class Click(models.Model):
    link = models.ForeignKey(
        Link,
        on_delete=models.CASCADE,
        related_name="clicks",
    )
    created_at = models.DateTimeField(auto_now_add=True)
    ip_hashed = models.CharField(max_length=64, blank=True, default="")
    referer = models.CharField(max_length=255, blank=True, default="")

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"Click en {self.link.short_code} @ {self.created_at}"
