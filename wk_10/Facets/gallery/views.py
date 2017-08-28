from django.shortcuts import render, redirect
from .models import Media
from .forms import MediaModelForm

def create(request):
    """
    Create a record for one type of media.  
    """
    if request.method == "GET":
        form = MediaModelForm()

    elif request.method == "POST":
        form = MediaModelForm(data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/gallery/thanks/')
            # This can also be used to send an email to the user.

    context = {'form': form}
    return render(request, 'create.html', context)


def thanks(request):
    return render(request, "thanks.html")
    
def retrieve(request, pk):
    """
    Retrieve media file/s.  
    """
    media = Media.objects.get(id=pk)
    context = {'media': media}
    return render(request, "index.html", context)

    
def update(request, pk):
    """
    Update the media file. 
    """
    media = Media.objects.get(id=pk)

    if request.method == "GET":
        form = MediaModelForm(instance=media)

    elif request.method == "POST":
        form = MediaModelForm(instance=media, data=request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            return redirect('/gallery/thanks/')
            # This can also be used to send an email to the user.

    context = {'form': form}
    return render(request, 'create.html', context)



def delete(request, pk):
    """
    Delete a media file.  
    """
    media = Media.objects.get(id=pk)
    media.delete()

    context = {'status': f'Deleted {media.id}'}
    return render(request, "index.html", context)


def display(request):
    """
    Display a media file.  
    """
    context = {}
    return render(request, "index.html", context)
