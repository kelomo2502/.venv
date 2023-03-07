from customers.models import Customers
from customers.serializers import CustomerSerializer
from django.http import JsonResponse

def customers(request):
    #Invoke serializer and return to client
    data = Customers.objects.all()
    serializer = CustomerSerializer(data, many = True)
    return JsonResponse({'customers': serializer.data})