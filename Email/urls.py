from django.conf.urls import *

from views import contato
from views import obrigado,contatomail

urlpatterns = patterns('',

   url(url(r'^$,arquivo),
   
   url(r'^contato/', 'views.contato', name='contato'),
   url(r'^obrigado/','views.obrigado', name='obrigado'),
   
   url(r'^contatomail/','views.contatomail', name='contatomail'),

          
          
)
