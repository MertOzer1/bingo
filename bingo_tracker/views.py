from django.shortcuts import render, redirect


# Create your views here.

from .models import BingoSheet
from django.http import HttpResponseRedirect
from django.urls import reverse



def index(request):
    sheets = BingoSheet.objects.all()
    called_numbers = request.session.get('called_numbers', [])
    return render(request, 'bingo_tracker/index.html', {
        'sheets': sheets,
        'number_range': range(1, 16),
        'called_numbers': called_numbers,
    })



def add_sheet(request):
    if request.method == 'POST':
        # Extracting numbers from the form
        numbers = [request.POST.get(f'number{i}') for i in range(1, 16)]
        
        # Create a new BingoSheet instance
        new_sheet = BingoSheet.objects.create(
            number1=numbers[0], number2=numbers[1], number3=numbers[2], 
            number4=numbers[3], number5=numbers[4], number6=numbers[5],
            number7=numbers[6], number8=numbers[7], number9=numbers[8],
            number10=numbers[9], number11=numbers[10], number12=numbers[11],
            number13=numbers[12], number14=numbers[13], number15=numbers[14]
        )
        new_sheet.save()

        # Redirect to the main page
        return redirect('index')

    # If not a POST request, just render the index page
    return render(request, 'bingo_tracker/index.html')



def enter_number(request):
    if request.method == 'POST':
        called_number = int(request.POST.get('called_number'))

        # Store called numbers in session
        if 'called_numbers' not in request.session:
            request.session['called_numbers'] = []
        request.session['called_numbers'].append(called_number)
        request.session.modified = True

        # Highlight matching numbers on sheets (additional implementation needed)

    return redirect('index')




def new_game(request):
    request.session['called_numbers'] = []
    return redirect('index')


def delete_sheet(request, sheet_id):
    if request.method == 'POST':
        sheet = BingoSheet.objects.get(id=sheet_id)
        sheet.delete()
        return HttpResponseRedirect(reverse('index'))