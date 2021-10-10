from django.contrib import admin
# Register your models here.
from .models import City, Language, Vacancy, Error, Url
#from .models import City, Language, Vacancy, Error, Url

admin.site.register(City)
admin.site.register(Language)
admin.site.register(Vacancy)
admin.site.register(Error)
admin.site.register(Url)