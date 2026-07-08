<p align="center">
  <img src="docs/screenshot.png" alt="URL Shortener screenshot" width="800">
</p>

<h1 align="center">django-url-shortener</h1>

<p align="center">
  <a href="https://acortador.moisesvalero.es">🌐 Demo</a> ·
  <a href="https://github.com/moisesvalero/django-url-shortener">📦 Repo</a>
</p>

---

## 🇪🇸 Español

Acortador de URLs moderno construido con **Django 5.2**, **HTMX** y **Tailwind CSS 3**, desplegado en **Vercel**.

**Demo en vivo:** [https://acortador.moisesvalero.es](https://acortador.moisesvalero.es)
**URLs cortas generadas via:** `https://a.moisesvalero.es/{codigo}`

### Características

- Acortamiento instantáneo con validación y deduplicación
- Interfaz reactiva vía HTMX (sin recarga de página)
- Copia al portapapeles con un clic
- Estadísticas de clics por enlace (IP hasheada, referer, timestamp)
- Rate limiting por IP para prevenir abuso
- Caché lazy-load para resolución rápida de URLs
- Diseño responsivo con modo oscuro y Material Design 3
- Postgres listo para producción, SQLite en desarrollo
- SSL/HTTPS forzado en producción
- Sin dependencias externas de tracking

### Stack

| Capa | Tecnología |
|---|---|
| **Backend** | Django 5.2 (Python 3.12) |
| **Frontend** | HTMX 2.x, Tailwind CSS 3, Material Symbols |
| **Base de datos** | PostgreSQL (Neon) / SQLite (dev) |
| **Estáticos** | Whitenoise |
| **Despliegue** | Vercel (serverless Python) |

### Inicio rápido (local)

```bash
git clone https://github.com/moisesvalero/django-url-shortener.git
cd django-url-shortener
uv sync
pnpm install && pnpm exec tailwindcss -i static/src/input.css -o static/dist/output.css --minify
uv run manage.py migrate
uv run manage.py runserver
# Abre http://localhost:8000
```

### Tests

```bash
uv run pytest -v --no-header
```

### Variables de entorno (`.env`)

```env
DJANGO_SECRET_KEY=<secreto>
DJANGO_DEBUG=True
BASE_URL=http://localhost:8000
ALLOWED_HOSTS=localhost,127.0.0.1,acortador.moisesvalero.es,a.moisesvalero.es
CSRF_TRUSTED_ORIGINS=http://localhost:8000,https://acortador.moisesvalero.es,https://a.moisesvalero.es
IP_HASH_SALT=<salt>
DATABASE_URL=postgresql://...
```

### API

```http
GET /api/resolve/{slug}/
# → { "url": "https://ejemplo.com/enlace" }

GET /health/
# → { "status": "ok" }
```

---

## 🇬🇧 English

Modern URL shortener built with **Django 5.2**, **HTMX**, and **Tailwind CSS 3**, deployed on **Vercel**.

**Live demo:** [https://acortador.moisesvalero.es](https://acortador.moisesvalero.es)
**Short URLs generated via:** `https://a.moisesvalero.es/{code}`

### Features

- Instant link shortening with validation and deduplication
- Reactive UI via HTMX (no full page reloads)
- One-click copy to clipboard
- Per-link click analytics (hashed IP, referrer, timestamp)
- Per-IP rate limiting to prevent abuse
- Lazy-load cache for fast URL resolution
- Responsive design with dark mode and Material Design 3
- Production-ready PostgreSQL, SQLite in development
- Enforced SSL/HTTPS in production
- No external tracking dependencies

### Tech Stack

| Layer | Technology |
|---|---|
| **Backend** | Django 5.2 (Python 3.12) |
| **Frontend** | HTMX 2.x, Tailwind CSS 3, Material Symbols |
| **Database** | PostgreSQL (Neon) / SQLite (dev) |
| **Static files** | Whitenoise |
| **Deployment** | Vercel (serverless Python) |

### Quick start (local)

```bash
git clone https://github.com/moisesvalero/django-url-shortener.git
cd django-url-shortener
uv sync
pnpm install && pnpm exec tailwindcss -i static/src/input.css -o static/dist/output.css --minify
uv run manage.py migrate
uv run manage.py runserver
# Open http://localhost:8000
```

### Tests

```bash
uv run pytest -v --no-header
```

### Environment variables (`.env`)

```env
DJANGO_SECRET_KEY=<secret>
DJANGO_DEBUG=True
BASE_URL=http://localhost:8000
ALLOWED_HOSTS=localhost,127.0.0.1,acortador.moisesvalero.es,a.moisesvalero.es
CSRF_TRUSTED_ORIGINS=http://localhost:8000,https://acortador.moisesvalero.es,https://a.moisesvalero.es
IP_HASH_SALT=<salt>
DATABASE_URL=postgresql://...
```

### API

```http
GET /api/resolve/{slug}/
# → { "url": "https://example.com/link" }

GET /health/
# → { "status": "ok" }
```

---

### Screenshot

Reemplaza `docs/screenshot.png` con una captura real del proyecto.

### License

MIT — hecho por [moisesvalero](https://moisesvalero.es)
