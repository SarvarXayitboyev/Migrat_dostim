from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import CityViewSet,EmbassyViewSet,CountryViewSet,UniversityViewSet,WorkViewSet,UserViewSet,OfferViewSet,HomeProblemViewSet,ToWorkCountryViewSet,ToStudyCountryViewSet,WorkCountryViewSet,StudyCountryViewSet,EmbassyByCountryViewSet,WorkCategoryViewSet


router = DefaultRouter()
router.register(r'city', CityViewSet, basename='city')
router.register(r'country_embassy', EmbassyByCountryViewSet, basename='country_embassy')
router.register(r'embassy', EmbassyViewSet, basename='embassy')
router.register(r'country', CountryViewSet, basename='country')
router.register(r'to_work_country', ToWorkCountryViewSet, basename='to_work_country')
router.register(r'to_study_country', ToStudyCountryViewSet, basename='to_study_country')
router.register(r'work_country', WorkCountryViewSet, basename='work_country')
router.register(r'study_country', StudyCountryViewSet, basename='study_country')
router.register(r'university', UniversityViewSet, basename='university')
router.register(r'work', WorkViewSet, basename='work')
router.register(r'work_category', WorkCategoryViewSet, basename='work_category')
router.register(r'user', UserViewSet, basename='user')
router.register(r'offer', OfferViewSet, basename='offer')
router.register(r'home_problem', HomeProblemViewSet, basename='home_problem')


urlpatterns = [
    path('api/v1/', include(router.urls)),
]