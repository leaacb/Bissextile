from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import service
from .serializers import YearSerializer, RangeYearSerializer, ArchiveSerializer
from .models import Archive
from .utils import get_utc_timestamp


class BissextileYear(APIView):
    def post(self, request):
        serializer = YearSerializer(data=request.data)

        if serializer.is_valid():
            year = serializer.data['value']
            isbissextile = service.bissextile(year)
            Archive.objects.create(
                endpoint='Year',
                date=get_utc_timestamp(),
                result=str(year)+' : ' + str(isbissextile)
            )
            return Response(isbissextile, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BissextileRangeYear(APIView):
    def post(self, request):
        serializer = RangeYearSerializer(data=request.data)

        if serializer.is_valid():
            first_year = serializer.data['first_year']
            second_year = serializer.data['second_year']
            if first_year > second_year:
                resultat = "Les annees de debut et de fin sont incorrectes"
                status_code = 400
            elif first_year == second_year:
                resultat = "Les annees de debut et de fin sont egales"
                status_code = 400
            else:
                liste_annee = [year for year in range(first_year, second_year + 1) if (
                                service.bissextile(year) is True)]
                resultat = liste_annee
                status_code = 201

            Archive.objects.create(
                endpoint="Year range",
                date=get_utc_timestamp(),
                result=resultat)
            return Response(resultat, status=status_code)
        else:
            return Response(serializer.errors, status=400)


@api_view(['GET'])
def endpoint_archives(request):
    if request.method == 'GET':
        historique = Archive.objects.all().order_by('-date')
        serializer = ArchiveSerializer(historique, many=True)
        return Response(serializer.data, status=200)
    else:
        return Response("Methode get obligatoire", status=405)
