# Acortador — AGENTS.md

Stack: Django 5.2, SQLite, HTMX, Tailwind CSS 3
Dominio: acortador.moisesvalero.es
Gestor: uv (Python), pnpm (Tailwind)
Tooling: ruff (lint/format), pytest (tests)

## Comandos

```powershell
uv run manage.py runserver          # dev
uv run manage.py check              # validación Django
uv run pytest -v --no-header        # tests
uv run ruff check .                 # lint
uv run ruff format --check .        # format
pnpm exec tailwindcss -i static/src/input.css -o static/dist/output.css --minify  # Tailwind build
```

## Deploy (productivo)

- `DJANGO_DEBUG=False`, definir todas las env vars
- SECRET_KEY, IP_HASH_SALT largos y aleatorios
- ALLOWED_HOSTS=acortador.moisesvalero.es
- CSRF_TRUSTED_ORIGINS=https://acortador.moisesvalero.es
- BASE_URL=https://acortador.moisesvalero.es
- Whitenoise sirve estáticos, Gunicorn como WSGI
- Migrar + collectstatic: `uv run manage.py migrate && uv run manage.py collectstatic --noinput`

## DNS

Registro CNAME apuntando acortador → URL del hosting (Railway/Render/Vercel).
