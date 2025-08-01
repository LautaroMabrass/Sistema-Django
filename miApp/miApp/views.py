from django.http import HttpResponse
from django.template import Template, Context

# Index vista
def index(request):
    docIndex = open("/home/victor/Escritorio/django-proyecto/miApp/plantillas/index.html")
    plt = Template(docIndex.read())
    docIndex.close()
    ctx = Context()
    documento = plt.render(ctx)
    return HttpResponse(documento)