# 
# It provides a way to get fully functional REST api 
# for my models adding only one line to urls.py
# see test1/urls.py
# 
# generates 
#  /test1/autorest/musician/
#  /test1/autorest/musician/<pk>
#  /test1/autorest/album/
#  /test1/autorest/album/<pk>
#  etc


import django.db
import re
from rest_framework import serializers, viewsets, routers


def snake_case(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()


def  rest_generator( models_module):

    router = routers.SimpleRouter()

    for class_name in dir(models_module):
        model = getattr(models_module, class_name)
        if type(model) != type(django.db.models.Model): continue
        
        # Generate Serializers
        serializer_name = class_name+'Serializer'
        serializer = type(
            serializer_name, 
            (serializers.ModelSerializer,),
            {
                'Meta': type(
                    'Meta', 
                    (object,), 
                    {
                        'fields' : '__all__',
                        'model'  : model
                    }
                ),
            }
        )

        # Make ViewSet
        view_name = class_name+'ViewSetAuto'
        view = type(
            view_name, 
            (viewsets.ModelViewSet,),
            {
                'queryset': model.objects.all(),
                'serializer_class' : serializer
            }
        )
        
        router.register( r'autorest/'+snake_case(class_name), view)
        
    return router.urls

