from django.shortcuts import render
from .models import IceCream

# Create your views here.
#FBV Function Based View (Request>URL>View)

def scream_maker(request):
    """
    Creates a new Ice Cream record in the database
    from user's submitted form data. 
    
    A view is a function that takes an HTTP request 
    and returns an HTTP response. 
    
    """


    pass
    return render(request, 'index.html')


def scream_taker(request, pk):
    """
    Creates a new Ice Cream record in the database
    from the url.  

    A view is a function that takes an HTTP request 
    and returns an HTTP response. 

    """
    icecream = IceCream.objects.get(pk=pk)
    context = {'scream': icecream}


    pass
    return render(request, 'index.html', context)