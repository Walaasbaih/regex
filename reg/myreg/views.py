
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Reg
from .serializers import *

@api_view(['GET', 'POST'])
def reg_list(request):
    if request.method == 'POST':
        dresult = re.match(request.data['expression'], request.data['text'])
        if result:
            return Response({"status": "Query String Is Valid", "result": "done"})
        else:
            return Response({"status": "Query String Is Invalid", "result": "No Result"})


