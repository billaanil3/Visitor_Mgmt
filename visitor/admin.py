from django.contrib import admin

# Register your models here.
from visitor.models import Country
from visitor.models import State
from .models import Location
from .models import User
from .models import Organization
from .models import Department
from .models import Visitor
from .models import Employee
from .models import VisitDetails

admin.site.register(Country)
admin.site.register(State)
