from django.contrib import admin
from .models import City,Embassy,Country,University,Work,User,Offer,HomeProblem,WorkCategory
# Register your models here.
admin.site.register(City)
admin.site.register(Embassy)
admin.site.register(Country)
admin.site.register(University)
admin.site.register(Work)
admin.site.register(WorkCategory)
admin.site.register(User)
admin.site.register(Offer)
admin.site.register(HomeProblem)