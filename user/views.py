from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .serializers import CitySerializer, EmbassySerializer, CountrySerializer, UniversitySerializer, WorkSerializer, \
    UserSerializer, OfferSerializer, HomeProblemSerializer, WorkCategory, WorkCategorySerializer
from .models import City, Embassy, Country, University, Work, User, Offer, HomeProblem,WorkCategory

# Create your views here.

class CityViewSet(viewsets.ModelViewSet):
    serializer_class = CitySerializer
    queryset = City.objects.all()

    class CityViewSet(viewsets.ModelViewSet):
        serializer_class = CitySerializer
        queryset = City.objects.all()

        def list(self, request, *args, **kwargs):
            # URL parametridan country_id ni olish
            country_id = request.query_params.get('country_id', None)

            if country_id:
                # country_id bo'yicha filtrlash
                cities = City.objects.filter(country_id=country_id)
            else:
                # Agar country_id bo'lmasa, barcha shaharlarni qaytarish
                cities = City.objects.all()

            serializer = CitySerializer(cities, many=True)
            return Response(serializer.data)



class EmbassyViewSet(viewsets.ModelViewSet):
    serializer_class = EmbassySerializer
    queryset = Embassy.objects.all()


class EmbassyByCountryViewSet(viewsets.ViewSet):

    def list(self, request):
        country_id = request.query_params.get('country_id', None)

        if country_id:
            embassies = Embassy.objects.filter(country_id=country_id)
            serializer = EmbassySerializer(embassies, many=True)
            return Response(serializer.data)
        else:
            return Response({"detail": "Country ID is required"}, status=400)


class CountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class ToWorkCountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.filter(to_work=True)


class ToStudyCountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.filter(to_study=True)


class WorkCountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.filter(work=True)


class StudyCountryViewSet(viewsets.ModelViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.filter(study=True)


class UniversityViewSet(viewsets.ModelViewSet):
    serializer_class = UniversitySerializer
    queryset = University.objects.all()

    def list(self, request, *args, **kwargs):
        city_id = request.query_params.get('city_id', None)

        if city_id:
            # city_id bo'yicha universitetlarni filtrlash
            universities = University.objects.filter(city_id=city_id)
        else:
            # Agar city_id bo'lmasa, barcha universitetlarni qaytarish
            universities = University.objects.all()

        serializer = UniversitySerializer(universities, many=True)
        return Response(serializer.data)


class WorkViewSet(viewsets.ModelViewSet):
    serializer_class = WorkSerializer
    queryset = Work.objects.all()

    def list(self, request, *args, **kwargs):
        category_id = request.query_params.get('category')
        queryset = self.get_queryset()  # Asl queryset ni olish
        if category_id:
            queryset = queryset.filter(category_id=category_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'chat_id'  # chat_id bo‘yicha qidirish uchun

    def retrieve(self, request, chat_id=None):
        user = get_object_or_404(User, chat_id=chat_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def list(self, request):
        chat_id = request.query_params.get('chat_id', None)
        if chat_id:
            user = get_object_or_404(User, chat_id=chat_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            users = User.objects.all()
            serializer = UserSerializer(users, many=True)
            return Response(serializer.data)


class OfferViewSet(viewsets.ModelViewSet):
    serializer_class = OfferSerializer
    queryset = Offer.objects.all()


class HomeProblemViewSet(viewsets.ModelViewSet):
    serializer_class = HomeProblemSerializer
    queryset = HomeProblem.objects.all()


class WorkCategoryViewSet(viewsets.ModelViewSet):
    serializer_class = WorkCategorySerializer
    queryset = WorkCategory.objects.all()


