from django.shortcuts import render

def contact_view(request):
    return render(request,"iletisim.html",{})