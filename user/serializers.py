from rest_framework import serializers
from .models import City,Country,Embassy,University,Work,User,Offer,HomeProblem,WorkCategory


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class EmbassySerializer(serializers.ModelSerializer):
    class Meta:
        model = Embassy
        fields = '__all__'


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class UniversitySerializer(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'


class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'chat_id', 'full_name', 'phone_number', 'location']
        ref_name = 'CustomUserSerializer'

class OfferSerializer(serializers.ModelSerializer):
    class Meta:
        model = Offer
        fields = '__all__'


class HomeProblemSerializer(serializers.ModelSerializer):
    class Meta:
        model = HomeProblem
        fields = '__all__'


class WorkCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkCategory
        fields = '__all__'