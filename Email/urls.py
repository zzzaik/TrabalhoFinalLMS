from django.conf.urls import *

from Email.views import contato,arquivo
from Email.views import obrigado,contatomail

urlpatterns = patterns('',

   url(url(r'^$,arquivo),
   
   url(r'^contato/', 'Email.views.contato', name='contato'),
   url(r'^obrigado/','Email.views.obrigado', name='obrigado'),
   
   url(r'^contatomail/','Email.views.contatomail', name='contatomail'),

          
          
)
