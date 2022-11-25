import datetime

from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from BaBaK_world_Agent import settings
from base.models import propertise, propertiseimg


def home(request):
    properties = propertise.objects.all()
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    context = {'properties': properties, 'year': year}
    return render(request, 'base/index.html', context)


def addlisting(request):
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        purpose = request.POST.get('purpose')
        price = request.POST.get('price')
        bedroom = request.POST.get('bedroom')
        bathroom = request.POST.get('bathroom')
        square_ft = request.POST.get('squareft')
        maplocation = request.POST.get('maplocation')
        head_line = request.POST.get('head_line')
        image = request.FILES.getlist('images')
        head_image = request.FILES.get('head_image')
        info = request.POST.get('info')
        ger = propertise(author=request.user, name=name, address=address, price=price, total_bedroom=bedroom,
                         squar_ft=square_ft, bathroom=bathroom, propertise_headline=head_line, purpose=purpose,
                         map_location=maplocation,
                         image=head_image, info=info)
        if ger:
            ger.save()
            for images in image:
                imgpro = propertiseimg(name=ger, image=images)
                imgpro.save()
    context = {'year': year}
    return render(request, 'base/Listing.html', context)


def listpage(request, pk):
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    proper = propertise.objects.get(id=pk)
    properi = proper.propertiseimg_set.all()
    if request.method == 'POST':
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        send_mail(subject=name, message=message + "\n \n" +
                                        "Customer Email Address: "
                                        + email + '\n \n' + 'Properties Headline :  ' + proper.propertise_headline
                                        + '\n \n' + " " + 'Address :  ' + proper.address + '\n \n' + 'About : ' + str(
            proper.info),
                  from_email=settings.EMAIL_HOST_USER,
                  recipient_list=['azeezadedeji638@gmail.com'])
        messages.success(request, 'Thank you for contacting us The admin will reach out to you soon')

    context = {'proper': proper, 'properi': properi, 'year': year}
    return render(request, 'base/listingpage.html', context)


def updatelistpage(request, pk):
    currentDateTime = datetime.datetime.now()
    date = currentDateTime.date()
    year = date.strftime("%Y")
    proper = propertise.objects.get(id=pk)
    properi = proper.propertiseimg_set.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        purpose = request.POST.get('purpose')
        price = request.POST.get('price')
        bedroom = request.POST.get('bedroom')
        bathroom = request.POST.get('bathroom')
        square_ft = request.POST.get('squareft')
        maplocation = request.POST.get('maplocation')
        head_line = request.POST.get('head_line')
        image = request.FILES.getlist('images')
        head_image = request.FILES.get('head_image')
        info = request.POST.get('info')
        proper.name = name
        proper.address = address
        proper.purpose = purpose
        proper.total_bedroom = bedroom
        proper.bathroom = bathroom
        proper.price = price
        proper.properties_hedaline = head_line
        proper.info = info
        proper.square_ft = square_ft
        proper.map_location = maplocation
        proper.save()
        messages.success(request, 'Update change successfully')
        return redirect('base:page', proper.id)

    context = {'proper': proper, 'properi': properi,'year':year}
    return render(request, 'base/updateListing.html', context)
