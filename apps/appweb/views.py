from django.shortcuts import render

def home(request):
    """
    index
    """
    # Número de visitas a esta vista, contadas en la variable de sesión
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    context = {
        'num_visits': num_visits,
    }

    return render(request, "index.html", context=context)
