from django.db.models import F
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_http_methods

from .models import Click, Link
from .services import (
    generate_short_code,
    hash_ip,
    is_rate_limited,
    set_cached_link,
)


def home(request):
    links = Link.objects.filter(is_active=True)[:10]
    return render(request, "shortener/home.html", {"links": links})


@require_http_methods(["POST"])
def create(request):
    url = request.POST.get("url", "").strip()

    if not url:
        return HttpResponseBadRequest("URL es requerida")

    if not (url.startswith("http://") or url.startswith("https://")):
        return HttpResponseBadRequest("Solo URLs http/https son permitidas")

    ip = request.META.get("REMOTE_ADDR", "")
    ip_hashed = hash_ip(ip)
    if is_rate_limited(ip_hashed):
        return HttpResponseBadRequest("Demasiadas peticiones. Espera un minuto.")

    link = Link.objects.filter(original_url=url, is_active=True).first()
    if link:
        return render(request, "shortener/partials/_link_card.html", {"link": link})

    link = Link.objects.create(original_url=url)
    link.short_code = generate_short_code(link.id)
    link.save(update_fields=["short_code"])

    set_cached_link(link.short_code, link.original_url)

    return render(request, "shortener/partials/_link_card.html", {"link": link})


def redirect_view(request, code):
    try:
        link = Link.objects.get(short_code=code, is_active=True)
    except Link.DoesNotExist:
        return HttpResponseNotFound("Link no encontrado")

    set_cached_link(link.short_code, link.original_url)

    ip = request.META.get("REMOTE_ADDR", "")
    referer = (request.META.get("HTTP_REFERER", "") or "")[:255]
    Click.objects.create(link=link, ip_hashed=hash_ip(ip), referer=referer)
    Link.objects.filter(id=link.id).update(clicks_count=F("clicks_count") + 1)

    return redirect(link.original_url)


def health(request):
    return JsonResponse({"status": "ok"})


@require_http_methods(["DELETE", "POST"])
def delete_link(request, code):
    deleted, _ = Link.objects.filter(short_code=code).delete()
    if deleted:
        return HttpResponse("")
    return HttpResponseNotFound("")
