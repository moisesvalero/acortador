<p align="center">
  <img src="docs/screenshot.jpg" alt="URL Shortener screenshot" width="800">
</p>

<h1 align="center">django-url-shortener</h1>

<p align="center">
  <a href="https://acortador.moisesvalero.es">🌐 Demo</a> ·
  <a href="https://github.com/moisesvalero/django-url-shortener">📦 Repo</a>
</p>

---

## 🇪🇸 Español

Acortador de URLs moderno y altamente optimizado construido con **Django 5.2**, **HTMX** y **Tailwind CSS 3**, diseñado para despliegues serverless rápidos en plataformas como **Vercel**.

**Demo en vivo:** [https://acortador.moisesvalero.es](https://acortador.moisesvalero.es)  
**URLs cortas generadas vía:** `https://a.moisesvalero.es/{codigo}`

### Características y Mejoras Implementadas

- **Optimización de Rendimiento con Caché (Cero Lecturas SQL en Redirección):** Las redirecciones de URLs cortas ahora interseptan la caché en memoria primero. Al almacenar tanto la URL original como el ID del enlace como una tupla `(link_id, original_url)`, se pueden registrar los clics de forma asíncrona y atómica sin hacer consultas de lectura (`SELECT`) a la base de datos de enlaces.
- **Rate Limiting Atómico Correcto:** Se corrigió un bug en la ventana de tiempo del limitador de tasa por IP. Ahora utiliza operaciones atómicas (`cache.add` e `incr` de Django) que garantizan que el TTL no se reinicie en cada petición sucesiva del usuario, limitando de forma estricta las ráfagas de peticiones abusivas (máximo 10 peticiones por minuto).
- **Validación de URLs de Entrada Robusta:** En lugar de comprobar simples prefijos, el acortador utiliza el `URLValidator` nativo de Django, asegurando que sólo se procesen y guarden en la base de datos URLs sintácticamente correctas y seguras.
- **Resolución de IP Real Detrás de Proxies:** Detección de IP adaptada para entornos de producción detrás de proxies y balanceadores de carga mediante la cabecera `HTTP_X_FORWARDED_FOR` con fallback a `REMOTE_ADDR`.
- **Validadores de Contraseñas Activos en Admin:** Se configuraron e implementaron los validadores estándar de Django para asegurar que las credenciales de administración superen los requisitos mínimos de seguridad contra ataques de fuerza bruta.
- **Integración de Calidad de Código:** Configuración automática de `Prettier`, `Husky` y `Lint-staged` para el formateo de plantillas HTML/CSS y validación del código antes de cada commit.

### Stack Técnico

| Capa                  | Tecnología                                                |
| --------------------- | --------------------------------------------------------- |
| **Backend**           | Django 5.2 (Python 3.11+)                                 |
| **Frontend**          | HTMX 2.0.4, Tailwind CSS 3, Material Symbols              |
| **Base de datos**     | PostgreSQL (Neon) / SQLite (desarrollo local)             |
| **Estáticos**         | Whitenoise                                                |
| **Despliegue**        | Vercel (serverless Python)                                |
| **Calidad / Linters** | Ruff (linter/format), Prettier (HTML/CSS), Pytest (tests) |

### Inicio rápido (local)

1. **Clonar e instalar dependencias:**

   ```bash
   git clone https://github.com/moisesvalero/django-url-shortener.git
   cd django-url-shortener
   uv sync
   pnpm install
   ```

2. **Compilar estáticos y CSS:**

   ```bash
   pnpm exec tailwindcss -i static/src/input.css -o static/dist/output.css --minify
   ```

3. **Ejecutar migraciones y arrancar:**
   ```bash
   uv run manage.py migrate
   uv run manage.py runserver
   # Abre http://localhost:8000 en tu navegador
   ```

### Tests y Calidad

Para ejecutar las pruebas unitarias y de integración del proyecto:

```bash
uv run python -m pytest -v --no-header
```

Para validar el formato y reglas de linter con Ruff:

```bash
uv run ruff check .
uv run ruff format --check .
```

---

## 🇬🇧 English

A modern and highly optimized URL shortener built with **Django 5.2**, **HTMX**, and **Tailwind CSS 3**, designed for serverless architectures deployed on **Vercel**.

**Live demo:** [https://acortador.moisesvalero.es](https://acortador.moisesvalero.es)  
**Short URLs generated via:** `https://a.moisesvalero.es/{code}`

### Implemented Features and Improvements

- **Cache Performance Optimization (Zero SQL Reads on Redirect):** Short URL redirects now fetch data from the memory cache first. By storing the original URL and the link ID as a tuple `(link_id, original_url)`, click logging is executed atomically without requiring any read query (`SELECT`) to the main Link database table.
- **Atomic Rate Limiting:** Fixed a bug in the IP rate limiting window. It now utilizes atomic cache operations (`cache.add` and `incr`) that ensure the TTL does not reset on successive user requests, strictly blocking abusive request spikes (max 10 requests per minute).
- **Robust URL Validation:** Instead of simple prefix checks, the shortener leverages Django's native `URLValidator` to guarantee only syntactically valid and secure URLs are stored and processed.
- **Real IP Resolution Behind Proxies:** Client IP detection parses the `HTTP_X_FORWARDED_FOR` header first, falling back to `REMOTE_ADDR` to accurately handle proxies and serverless environments.
- **Active Password Validators in Admin:** Restored standard Django password validators to enforce secure administrative credentials and protect against brute-force attacks.
- **Quality Tooling Integration:** Configured `Prettier`, `Husky`, and `Lint-staged` to enforce HTML/CSS formatting and validate code quality on every commit.

### Tech Stack

| Layer                 | Technology                                                |
| --------------------- | --------------------------------------------------------- |
| **Backend**           | Django 5.2 (Python 3.11+)                                 |
| **Frontend**          | HTMX 2.0.4, Tailwind CSS 3, Material Symbols              |
| **Database**          | PostgreSQL (Neon) / SQLite (local dev)                    |
| **Static files**      | Whitenoise                                                |
| **Deployment**        | Vercel (serverless Python)                                |
| **Quality / Linters** | Ruff (linter/format), Prettier (HTML/CSS), Pytest (tests) |

### Quick start (local)

1. **Clone and install dependencies:**

   ```bash
   git clone https://github.com/moisesvalero/django-url-shortener.git
   cd django-url-shortener
   uv sync
   pnpm install
   ```

2. **Build static assets and CSS:**

   ```bash
   pnpm exec tailwindcss -i static/src/input.css -o static/dist/output.css --minify
   ```

3. **Run migrations and start server:**
   ```bash
   uv run manage.py migrate
   uv run manage.py runserver
   # Open http://localhost:8000 in your browser
   ```

### Tests and Quality Checks

To run the unit and integration test suite:

```bash
uv run python -m pytest -v --no-header
```

To validate code formatting and rules with Ruff:

```bash
uv run ruff check .
uv run ruff format --check .
```

---

### License

MIT — built with ❤️ by [moisesvalero](https://moisesvalero.es)
