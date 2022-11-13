from django.shortcuts import render
from django.http import HttpResponse
from gs_app.models import Character, Property, Weapon
import json

# Create your views here.
def character(request):
    response = {}
    characters = Character.objects.all()
    for item in characters:
        temp = {
            'id': item.id,
            'name': item.name,
            'element': item.element,
            'type': item.type,
            'mode': item.mode,
        }

        for i in range(0, 3):
            property = Property.objects.get(name_id=item.id, Lv=70+10*i)
            if property:
                key = 'propertyLv{x}'.format(x=property.Lv)
                dic = {
                    'baseHP': property.baseHP,
                    'baseATK': property.baseATK,
                    'baseDEF': property.baseDEF,
                }
                temp[key] = dic
        
        response[item.id] = temp
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')


def weapon(request):
    response = {}
    weapons = Weapon.objects.all()
    for item in weapons:
        temp = {
            'id': item.id,
            'name': item.name,
            'type': item.type,
            'baseATK': item.baseATK,
        }
        response[item.id] = temp
    return HttpResponse(json.dumps(response, ensure_ascii=False), content_type='application/json')
