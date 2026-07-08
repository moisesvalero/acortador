import os
from pathlib import Path

import django
import jazzmin
from django.conf import settings
from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "acortador.settings")

django_app = get_wsgi_application()

# WhiteNoise envuelve la app. En serverless (Vercel) servimos los
# archivos directamente desde STATICFILES_DIRS sin collectstatic
# (Vercel no persiste /tmp entre cold starts).
application = WhiteNoise(django_app)
for static_dir in settings.STATICFILES_DIRS:
    application.add_files(str(static_dir), prefix=settings.STATIC_URL)

# Estáticos del admin de Django + jazzmin
# jazzmin trae sus propios vendor/ (adminlte, fontawesome, bootstrap)
# que se sirven bajo /static/vendor/, /static/jazzmin/ y /static/admin/.
# El path completo de jazzmin cubre todo eso.
_jazzmin_static = Path(jazzmin.__file__).parent / "static"
if _jazzmin_static.is_dir():
    application.add_files(str(_jazzmin_static), prefix="static/")
_admin_static = Path(django.__file__).parent / "contrib" / "admin" / "static" / "admin"
if _admin_static.is_dir():
    application.add_files(str(_admin_static), prefix="static/admin/")

# En Vercel serverless, ejecuta migrations al arrancar en frío
if os.environ.get("VERCEL") and os.environ.get("DATABASE_URL"):
    from django.core.management import call_command

    call_command("migrate", "--noinput")
