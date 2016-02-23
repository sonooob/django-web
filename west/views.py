from django.http import HttpResponse

def first_page(request):
    return HttpResponse("西餐")