from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .scrapingCode import Scrap
# Create your views here.

class ShowResult(APIView):
    def post(self,request):
        try:
            data = request.data
            getKey = list(data.keys())[0]
            print(getKey)
            output = Scrap(data[getKey])
            finalResponse = {
                "statusCode" : "200",
                "data" : output,
                "totalCount" : len(output)
            }
            return Response(finalResponse ,status=status.HTTP_200_OK)
        except :
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)