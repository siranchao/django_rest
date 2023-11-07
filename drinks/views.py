from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer



def drink_list(request):
    # get all the drinks and serialize them
    drinks = Drink.objects.all()
    serializer = DrinkSerializer(drinks, many=True)

    return JsonResponse(serializer.data, safe=False)