from django.contrib.auth.models import Group, User
from rest_framework import permissions, viewsets
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated

from .models import Sample
from .serializers import GroupSerializer, UserSerializer, SampleSerializer, SampleResponseSerializer
from django.http import Http404, JsonResponse
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import check_password

from .utils import Bacteria, BacteriaService


class SampleView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        data = request.data
        serializer = SampleSerializer(data=data)

        if serializer.is_valid():
            sample_instance = serializer.save()
            sample_instance.users.add(request.user)
            sample_instance.save()
            return Response(status=201)
        return Response(serializer.errors, status=400)


class SampleSearchView(APIView):
    parser_classes = [JSONParser]

    def post(self, request):
        samples = Sample.objects.all().filter(users__id=request.user.id)
        serializer = SampleResponseSerializer(samples, many=True)
        return Response(serializer.data)


class SampleGetView(APIView):
    parser_classes = [JSONParser]

    def get(self, request, id):
        sample = Sample.objects.get(pk=id)
        if request.user not in sample.users.all():
            return Response(status=404)
        serializer = SampleSerializer(sample)
        return Response(serializer.data)


class SampleResultView(APIView):
    parser_classes = [JSONParser]

    def get(self, request, id):
        sample = Sample.objects.get(pk=id)
        if request.user not in sample.users.all():
            return Response(status=404)
        a = Bacteria(pop=sample.pop_a, ab=sample.ab_a, ac=sample.ac_a, ad=sample.ad_a,
                     ae=sample.ae_a, k=sample.k_a, r=sample.r_a)
        b = Bacteria(pop=sample.pop_b, ab=sample.ab_b, ac=sample.ac_b, ad=sample.ad_b,
                     ae=sample.ae_b, k=sample.k_b, r=sample.r_b)
        c = Bacteria(pop=sample.pop_c, ab=sample.ab_c, ac=sample.ac_c, ad=sample.ad_c,
                     ae=sample.ae_c, k=sample.k_c, r=sample.r_c)
        d = Bacteria(pop=sample.pop_d, ab=sample.ab_d, ac=sample.ac_d, ad=sample.ad_d,
                     ae=sample.ae_d, k=sample.k_d, r=sample.r_d)
        e = Bacteria(pop=sample.pop_e, ab=sample.ab_e, ac=sample.ac_e, ad=sample.ad_e,
                     ae=sample.ae_e, k=sample.k_e, r=sample.r_e)
        calculator = BacteriaService()
        resultado = calculator.ode45(a, b, c, d, e, 1000)
        return Response(resultado)
