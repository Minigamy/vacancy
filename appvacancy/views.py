from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseServerError


def main_view(request, id):
    return render(request, 'appvacancy/vacancylist.html')


def vacancy_view(request, idd):
    return render(request, 'appvacancy/onevacancy.html')
