from django.shortcuts import render

# Create your views here.
def jinja_operation(request):
    return render(request,'jinja_operation.html')