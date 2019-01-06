from django.urls import include, path
from autorest import rest_generator
import test1.models

urlpatterns = [
	# ...something
]

urlpatterns += rest_generator(test1.models)
