from django.shortcuts import render
import pandas as pd
import json
from django.http import JsonResponse
# Create your views here.

df = pd.read_csv('home/restaurants_small.csv')


def index(request):
    if request.method == "POST":
        data = request.POST.get('search')
        my_dict = []
        try:
            for i in range(df.shape[0]):
                dishes = json.loads(df.iloc[i, 3])
                my_dishes = []
                for dish, price in dishes.items():
                    if(data in dish):
                        my_dishes.append({'name': dish, 'price': price})
                if my_dishes != []:
                    my_dict.append(
                        {'restorant_name': df.iloc[i, 1], 'dishes': my_dishes})
            return_json_data = json.dumps({
                'data': my_dict,
                'status': 200
            }
            )
        except Exception:
            return_json_data = json.dumps({
                'status': 404
            }
            )
        finally:
            return JsonResponse(return_json_data, safe=False)
    return render(request, 'home/index.html')
