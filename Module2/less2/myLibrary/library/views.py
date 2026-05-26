from django.http import HttpResponse

from .models import Books``


def home(request):
    return HttpResponse('hello library')

def books(request):
    books =Books.objects.all()
    output = '<br>'.join([str(book) for book in books])
    return HttpResponse(output)


def create_book(request):
    new_book = Books(**request.POST.dict())
    new_book.save()
    return HttpResponse("Book created")