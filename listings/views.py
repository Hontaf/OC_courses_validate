from django.shortcuts import render,redirect,reverse
from django.core.mail import send_mail

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .models import Band 
from .models import Listing
from .forms import ContactUsForm,BandForm,ListingForm
# Create your views here.

def hello(request):
    bands = Band.objects.all()
    return render(request,"listings/hello.html", {"bands":bands})

def about(request):
    return render(request,"listings/about.html")

def listings(request):
    listings = Listing.objects.all()
    return render(request,"listings/listings.html",{"listings":listings})

def contact(request):
    if request.method == 'POST':
         # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
        if form.is_valid():
                send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
                return redirect('email_sent') 
        # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
        # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

        else:
            # ceci doit être une requête GET, donc créer un formulaire vide
            form = ContactUsForm()

    form = ContactUsForm()
    return render(request,"listings/contact.html",
                    {'form':form})

def band_list(request):
    bands = Band.objects.all()
    return render(request,
            'listings/band_list.html',
            {'bands':bands})

#la vue detail :
def band_detail(request,id):
    band = Band.objects.get(id=id)#on envoie en plus du request l'id en parametres 
    return render(request,
            'listings/bands_detail.html',
            {'band':band})

#liste des annonces listings:
def listing_list(request):
    listings = Listing.objects.all()
    return render(request,
            'listings/listings_list.html',
            {'listings':listings})
#detail listing 

def listing_detail(request,id):
    listing = Listing.objects.get(id=id)
    return render(request,
                    'listings/listings_detail.html',
                    {'listing':listing})

def email_sent(request):
    return render (request,"listings/email_sent.html")
#une fonction qui retourne le c=formulaire de contact 

def bands_create(request):
     if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

     else:
        form = BandForm()
     return render (request,
                    'listings/bands_add.html',
                    {'form':form})

def listings_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save()
            return redirect('listing-detail',listing.id)
    else:
        form = ListingForm()
    return render (request,
                    'listings/listings_add.html',
                    {'form':form})

def bands_change(request,id):
    band = Band.objects.get(id=id)
    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)  
    return render(request,
        'listings/band_change.html',
        {'form':form})

def listings_change(request,id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        form = ListingForm(request.POST,instance=listing)
        if form.is_valid():
            form.save()
            return redirect('listing-detail',listing.id)
    else:
        form = ListingForm(instance=listing)
    return render(request,
                   'listings/listing_change.html',
                   {'form':form} )

# listings/views.py
def band_delete(request, id):
    band = Band.objects.get(id=id)  # nécessaire pour GET et pour POST

    if request.method == 'POST':
    # supprimer le groupe de la base de données
        band.delete()
        # rediriger vers la liste des groupes
        return HttpResponseRedirect(reverse('band-list'))

# pas besoin de « else » ici. Si c'est une demande GET, continuez simplement

    return render(request,
                'listings/bands_delete.html',
                {'band': band})

def listing_delete(request,id):
    listing = Listing.objects.get(id=id)
    if request.method == 'POST':
        listing.delete()
        return HttpResponseRedirect(reverse('listing-list'))
    return render(request,
                    'listings/listing_delete.html',
                    {'listing':listing})