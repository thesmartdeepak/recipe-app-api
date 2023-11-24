'''Write API calling'''
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from app.services import add_two_numbers

class APICalling(APIView):

    def get(self, request):
        result_sum = add_two_numbers(request.GET.get('x'), request.GET.get('y'))
        print("result_sum", result_sum)
        return Response(result_sum)