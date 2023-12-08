from rest_framework import routers

from .views import (MeViewSet, ProjectViewSet, PricingViewSet, SkillViewSet, ContactViewSet)

router = routers.DefaultRouter()

router.register(r'api/me', MeViewSet, basename ='me')
router.register(r'api/projects', ProjectViewSet, basename ='projects')
router.register(r'api/pricings', PricingViewSet, basename ='pricings')
router.register(r'api/skills', SkillViewSet, basename ='skills')
router.register(r'api/contacts', ContactViewSet, basename ='contacts')

urlpatterns = router.urls

