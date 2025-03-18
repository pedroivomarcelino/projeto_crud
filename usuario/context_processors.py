from .models import Usuario

def usuario_logado(request):
    usuario = None
    if request.session.get('usuario_logado'):
        usuario_id = request.session['usuario_logado']
        usuario = Usuario.objects.filter(id=usuario_id).first()
        
    return {'usuario': usuario}
