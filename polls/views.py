import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import service
from .serializers import YearSerializer, RangeYearSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import time
from .models import Archive
from .utils import get_utc_timestamp

archive = []  # on déclare notre historique


class BissextileYear(APIView):
    def post(self, request):
        serializer = YearSerializer(data=request.data)

        if serializer.is_valid():
            year = serializer.data['value']
            isbissextile = service.bissextile(year)
            result = {
                'endpoint': 'Annee Bissextile',
                'date': get_utc_timestamp(),
                'result': {'Annee Bissextile': isbissextile}
            }
            archive.append(result)
            Archive.objects.create(
                endpoint='Annee Bissextile',
                date=get_utc_timestamp(),
                result={'AnneeBissextile': isbissextile}
            )
            return Response({'isbissextile': isbissextile}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BissextileRangeYear(APIView):
    def post(self, request):
        serializer = RangeYearSerializer(data=request.data)

        if serializer.is_valid():
            first_year = serializer.data['first_year']
            second_year = serializer.data['second_year']
            if (first_year < second_year) and (first_year != second_year):
                liste_annee = [year for year in range(first_year, second_year + 1) if (
                                service.bissextile(year) is True)]
                result = {
                    'endpoint': "range_year d'annees",
                    'date': get_utc_timestamp(),
                    'result': {'Annees bissextiles': liste_annee}
                    }
                archive.append(result)
                Archive.objects.create(
                    endpoint='range_year d annees',
                    date=get_utc_timestamp(),
                    result={'Annee Bissextile': liste_annee}
                    )
                return Response({'Annees bissextiles': liste_annee}, status=201)
            else:
                result = {
                    'endpoint': 'range_year d annee',
                    'date': get_utc_timestamp(),
                    'result': 'Les annees de debut et de fin sont incorrectes.'
                    }
                archive.append(result)
                Archive.objects.create(
                    endpoint='Range d annees',
                    date=get_utc_timestamp(),
                    result='Les annees de debut et de fin sont incorrectes'
                    )
                return Response({'error': 'Les annees de debut et de fin sont incorrectes.'}, status=400)
        else:
            return Response({'error': 'Invalid Serializer'}, status=400)


@csrf_exempt
def endpoint_archives(request):
    if request.method == 'GET':
        return JsonResponse({'Archive': archive})
    else:
        return JsonResponse({'error'}, status=405)
