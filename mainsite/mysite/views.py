
from django.shortcuts import render
from .forms import PaymentForm

def payment_page(request):
	form = PaymentForm(request.POST or None)
	donation = request.POST.get('donation')
	print(donation)
	try:
		donation = int(donation) * 100  # Note 1 Rs == 100 ps
		donation = str(donation)
	except TypeError: 
                donation = 100     
   #	If delete this you will TypeError Razorpay money should be greater than 1 ps 
	return render(request, 'mysite/payment_page.html', {'form':form, 'donation':donation})
