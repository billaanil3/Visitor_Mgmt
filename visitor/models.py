from django.db import models
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from phone_field import PhoneField

# Create your models here.

class Country(models.Model):
    # countryName = CountryField()
    countryName = models.CharField(max_length=126, unique=True)
    countryCode = models.CharField(max_length=3, unique=True)


class State(models.Model):
    stateName = models.CharField(max_length=126, unique=True)
    country = models.ForeignKey(Country)


class Location(models.Model):
    locationName = models.CharField(max_length=126, unique=True)
    state = models.ForeignKey(State)


class User(models.Model):
    firstName = models.CharField(max_length=50, blank=False, null=False)
    lastName = models.CharField(max_length=50, blank=True, null=True)
    # pip install django-phone-field
    mobileNumber = PhoneField(blank=True, help_text='Contact phone number')


class Organization(models.Model):
    OrganizationName = models.CharField(max_length=126, unique=True)
    OrganizationAbbr = models.CharField(max_length=3, unique=True)
    country = models.ForeignKey(Country)
    state = models.ForeignKey(State)
    location = models.ForeignKey(Location)
    organizationAddress = models.TextField(max_length=256)
    pincode = models.IntegerField(max_length=6)


class Department(models.Model):
    departmentName = models.CharField(max_length=126, unique=True)
    employeeCount = models.IntegerField(max_length=10, default=0)
    organization = models.ForeignKey(Organization)


class Visitor(models.Model):
    visitorName = models.OneToOneField(User)
    visitorDriverLicenseNumber = models.IntegerField(max_length=50)
    visitorCompanyName = models.CharField(max_length=126)
    comingFrom = models.CharField(max_length=126, blank=False, null=False)


class Employee(models.Model):
    employeeName = models.OneToOneField(User)
    employeeCode = models.CharField(max_length=5, unique=True)
    department = models.ManyToManyField(Department)
    designation = models.CharField(max_length=50, blank=False, null=False)


class VisitDetails(models.Model):
    visitor = models.ForeignKey(Visitor)
    employee = models.ForeignKey(Employee)
    visitDate = models.DateTimeField(blank=False, null=False)
    purposeOfVisit = models.CharField(max_length=256, blank=False, null=False)
    visiDuration = models.CharField(max_length=50, blank=False, null=False)
    comments = models.TextField(max_length=256)
