      return HttpResponde(html)
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
        
