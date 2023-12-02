from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import joblib

@api_view(['GET'])
def test(request):
    return JsonResponse({'message': 'Success'})