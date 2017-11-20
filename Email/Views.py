from django.template import loader, Context
from django.http import HttpResponse
from django.shortcuts import render
from Email.models import EmailPost
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect
from forms import Formulario
from django.template import RequestContext
from django.core.mail import mailMensage


def arquivo(request):
    posts = EmailPost.objects.all()
    mi_template = loader.get_template("arquivo.html")
    mi_contexto = Context({'posts':posts})
    return HttpResponse(mi_template.render(mi_contexto))

def contato(request):
    if request.method == 'POST': # valida se o formulario foi enviado
       form = Formulario(request.POST)
       if form.is_valid(): # Valida se os dados estão sendo processado 
          return HttpResponseRedirect  
('/SuaPasta/Email/obrigado/') # redireciona para E-mail enviado com sucesso
    else:
        form = Formulario()
    
    return render(request, 'contato.html',{
        'form':form,
    })

def obrigado(request):
    html = <'html><body> Seu e-mail foi enviado com sucesso !!</body></html>'
    return HttpResponse(html)
    
    
def contatomail(request):
    if request.method == 'POST':
        formulario = FormularioContato(request.POST)
        if formulario.is_valid():
            assunto = 'esta e uma mensagem de teste do formulario'
            mensagem = formulario.cleaned_data['mensagem']
            mail = Emailmensage(assunto, mensagem, to=['seuemailaqui@gmail.com'])
            mail.send()
        return HttpResponseRedirect('/')
        
    else:
        formulario = FormularioContato()
    
    return render_to_response('contato_mail_html', {'formulario': formulario},
                              context_instance=RequestContext(request))
        
