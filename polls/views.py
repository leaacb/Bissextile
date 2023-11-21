import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Year
from .serializers import YearSerializer
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import time
from .models import Archive

archive = []  # on déclare notre historique

# étant donnée l'interdiction d'utiliser une librairie de date, nous allons formater une heure en temps universel coordonné (UTC)
# On utilise la méthode 'format' sur une chaine de caractère. {:04d} représente l'année avec au moins 4 chiffres, {:02d} le mois avec au moins 2 chiffres
#{:02d} le jour avec au moins deux chiffres etc jusqu'au minute( des zéros seront ajoutés en tête de chaîne au besoin ! ). Il s'agit d'espaces réservés.
# apres cela la méthode format remplace les {:04d} etc par les attributs tm_year etc...


def get_utc_timestamp():
    utc_time = time.gmtime()
    timestamp = "{:04d}-{:02d}-{:02d} {:02d}:{:02d}:{:02d} UTC".format(
        utc_time.tm_year, utc_time.tm_mon, utc_time.tm_mday,
        utc_time.tm_hour, utc_time.tm_min, utc_time.tm_sec
    )
    return timestamp

class BissextileYear(APIView):
    def post(self, request):
        serializer = YearSerializer(data=request.data)

        if serializer.is_valid():
            year = Year(value=serializer.data['value'])
            isbissextile = year.bissextile()
            result = {
                'endpoint': 'Annee Bissextile',
                'date': get_utc_timestamp(),
                'result': {'Annee Bissextile': isbissextile}
            }
            archive.append(result)
            Archive.objects.create(
                endpoint='Annee Bissextile',
                date=get_utc_timestamp(),
                result={'AnneeBissextile': {isbissextile}}
            )
            return Response({'isbissextile': isbissextile}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def bissextile_range(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        first_year_str = str(data.get("first_year"))
        second_year_str = str(data.get("second_year"))

        if first_year_str is not None and second_year_str is not None:
            first_year = int(first_year_str)
            second_year = int(second_year_str)
            if (first_year < second_year) and (first_year != second_year):
                liste_annee = [year for year in range(first_year, second_year + 1) if ((year % 4 == 0 and year % 100 != 0) or (year % 4 == 0 and year % 100 == 0 and year % 400 == 0))]
                result = {
                    'endpoint': 'Range d annees',
                    'date': get_utc_timestamp(),
                    'result': {'Annees bissextiles': liste_annee}
                }
                archive.append(result)
                Archive.objects.create(
                    endpoint='Range d annees',
                    date=get_utc_timestamp(),
                    result={'Annee Bissextile': liste_annee}
                )
                return JsonResponse({'Annees bissextiles': liste_annee})
            else:
                result = {
                    'endpoint': 'Range d annee',
                    'date': get_utc_timestamp(),
                    'result': 'Les annees de debut et de fin sont incorrectes.'
                }
                archive.append(result)
                Archive.objects.create(
                    endpoint='Range d annees',
                    date=get_utc_timestamp(),
                    result='Les annees de debut et de fin sont incorrectes'
                )
                return JsonResponse({'error': 'Les annees de debut et de fin sont incorrectes.'}, status=400)
        else:
            return JsonResponse({'error': 'Veuillez spécifier vos annees de début et de fin.'}, status=400)


@csrf_exempt
def endpoint_archives(request):
    if request.method == 'GET':
        return JsonResponse({'Archive': archive})
    else:
        return JsonResponse({'error'}, status=405)
