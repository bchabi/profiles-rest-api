from rest_framework.views import APIView
from rest_framework.response import Response


class HelloApiView(APIView):
    """TEST API View"""

    def get(self, request, format=None):
        """Return a list of APIVIEW features"""
        an_apiview = [
            'Uses HTTP Methods as function (get,post,patch,put,delete)',
            'gives you the most control over your application logic',
            'Is mapped manually to URLs'
        ]

        return Response({'message': 'hello!', 'an_apiview': an_apiview})
