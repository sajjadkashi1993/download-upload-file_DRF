from rest_framework.routers import SimpleRouter
from .api_views   import FileView
router = SimpleRouter()
router.register('files', FileView)


urlpatterns = router.urls
