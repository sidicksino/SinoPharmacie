from django.shortcuts import render
from django.db.models import Q
from .models import Pharmacy, Product

def home(request):
    """
    Renders the homepage with featured pharmacies and products.
    Handles search functionality via 'q' query parameter.
    """
    query = request.GET.get('q')
    
    # Base queries for verified pharmacies and available products
    pharmacies = Pharmacy.objects.filter(is_verified=True)
    products = Product.objects.filter(is_available=True, stock_quantity__gt=0)
    
    if query:
        # Search functionality
        pharmacies = pharmacies.filter(name__icontains=query)
        products = products.filter(
            Q(name__icontains=query) | 
            Q(category__icontains=query) |
            Q(description__icontains=query)
        )
    else:
        # Featured sections (limit results)
        pharmacies = pharmacies[:8]
        products = products.order_by('?')[:12] # Randomize featured products slightly
        
    context = {
        'pharmacies': pharmacies,
        'products': products,
        'search_query': query,
    }
    context = {
        'pharmacies': pharmacies,
        'products': products,
        'search_query': query,
    }
    return render(request, 'core/home.html', context)

from .forms import RegisterForm

def register(request):
    """
    Handles user registration using custom RegisterForm.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Auto-login after registration
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'core/register.html', {'form': form})
