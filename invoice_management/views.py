from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# For Report Lab
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.pagesizes import landscape
from reportlab.platypus import Image
# End for report lab


# Create your views here.

def home(request):
    title = ''
    context = {
        'title': title,
    }
    return render(request, "home.html", context)



def loginPage(request):
	if request.user.is_authenticated:
		return redirect('list_invoice')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('login')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('home')


def appointment(request):
    if request.method == "POST":

        your_name = request.POST['your-name']
        your_email = request.POST['your-email']
        your_car_type = request.POST['your-car-type']
        your_date = request.POST['your-date']
        your_message = request.POST['your-message']

        message = f'Appointment from {your_name}. Date: {your_date}, Query: {your_car_type}, Message: {your_message} '

        send_mail(
            f'Appointment from {your_name}',
            message,
            your_email,
            ['admin@email.co.za']
        )

        return render(request, "appointment.html", { 'your_name': your_name})
    else:
        return render(request, "home.html", {})

@login_required(login_url='login')
def list_invoice(request):
    title = 'list of Invoices'
    queryset = Invoice.objects.all()
    form = InvoiceSearchForm(request.POST or None)
    context = {
        'title': title,
        'queryset': queryset,
        'form': form,
    }
    if request.method == 'POST':
        queryset = Invoice.objects.filter(invoice_number__icontains = form['invoice_number'].value(), name__icontains = form['name'].value() )

    context = {
        'title': title,
        'queryset': queryset,
        'form': form,
    }

    if form['generate_invoice'].value() == True:
        instance = queryset
        data_file = instance
        num_of_invoices = len(queryset)
        message = str(num_of_invoices) + " invoices successfully generated."
        messages.success(request, message)

        def import_data(data_file):
            invoice_data = data_file
            for row in invoice_data:
                invoice_type = row.invoice_type
                invoice_number = row.invoice_number
                invoice_date = row.invoice_date
                name = row.name
                phone_number = row.phone_number

                line_one = row.line_one
                line_one_quantity = row.line_one_quantity
                line_one_unit_price = row.line_one_unit_price
                line_one_total_price = row.line_one_total_price

                line_two = row.line_two
                line_two_quantity = row.line_two_quantity
                line_two_unit_price = row.line_two_unit_price
                line_two_total_price = row.line_two_total_price

                line_three = row.line_three
                line_three_quantity = row.line_three_quantity
                line_three_unit_price = row.line_three_unit_price
                line_three_total_price = row.line_three_total_price

                line_four = row.line_four
                line_four_quantity = row.line_four_quantity
                line_four_unit_price = row.line_four_unit_price
                line_four_total_price = row.line_four_total_price

                line_five = row.line_five
                line_five_quantity = row.line_five_quantity
                line_five_unit_price = row.line_five_unit_price
                line_five_total_price = row.line_five_total_price


                total = row.total
                pdf_file_name = str(invoice_number) + '_' + str(name) + '.pdf'
                generate_invoice(str(name), str(invoice_number), 
                    str(line_one), str(line_one_quantity), str(line_one_unit_price), 
                    str(line_one_total_price), str(line_two), str(line_two_quantity),
                    str(line_two_unit_price), str(line_two_total_price), str(line_three),
                    str(line_three_quantity), str(line_three_unit_price),
                    str(line_three_total_price), str(line_four), str(line_four_quantity),
                    str(line_four_unit_price), str(line_four_total_price),  str(line_five),
                    str(line_five_quantity), str(line_five_unit_price),
                    str(line_five_total_price),
                    
                    str(total), str(phone_number), str(invoice_date),
                    str(invoice_type), pdf_file_name)

        def generate_invoice(name, invoice_number, 
                line_one, line_one_quantity, line_one_unit_price, line_one_total_price, 
                line_two, line_two_quantity, line_two_unit_price, line_two_total_price, 
                line_three, line_three_quantity, line_three_unit_price, line_three_total_price, 
                line_four, line_four_quantity, line_four_unit_price, line_four_total_price, 
                line_five, line_five_quantity, line_five_unit_price, line_five_total_price, 
                total, phone_number, invoice_date, invoice_type, pdf_file_name):
            c = canvas.Canvas(pdf_file_name)

            # image of seal

            logo = 'logobrix.jpg'
            c.drawImage(logo, 50, 700, width=500, height=120)

            c.setFont('Helvetica', 12, leading=None)
            # if invoice_type == 'Receipt':
            # 	c.drawCentredString(400, 660, "Receipt Number #:")
            # elif invoice_type == 'Proforma Invoice':
            # 	c.drawCentredString(400, 660, "Proforma Invoice #:")
            # else:
            c.drawCentredString(400, 660, str(invoice_type) + ':')
            c.setFont('Helvetica', 12, leading=None)
            invoice_number_string = str('0000' + invoice_number)
            c.drawCentredString(490, 660, invoice_number_string)


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(409, 640, "Date:")
            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(492, 641, invoice_date)


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(397, 620, "Amount:")
            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(484, 622, 'R '+total)


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(80, 660, "To:")
            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(150, 660, name)

            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(98, 640, "Phone #:")
            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(150, 640, phone_number)     

            c.setFont('Helvetica-Bold', 14, leading=None)
            c.drawCentredString(310, 580, str(invoice_type))
            c.drawCentredString(110, 560, "Particulars:")
            c.drawCentredString(295, 510, "__________________________________________________________")
            c.drawCentredString(295, 480, "__________________________________________________________")
            c.drawCentredString(295, 450, "__________________________________________________________")
            c.drawCentredString(295, 420, "__________________________________________________________")
            c.drawCentredString(295, 390, "__________________________________________________________")
            c.drawCentredString(295, 360, "__________________________________________________________")
            c.drawCentredString(295, 330, "__________________________________________________________")
            c.drawCentredString(295, 300, "__________________________________________________________")
            c.drawCentredString(295, 270, "__________________________________________________________")
            c.drawCentredString(295, 240, "__________________________________________________________")
            c.drawCentredString(295, 210, "__________________________________________________________")

            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(110, 520, 'ITEMS')     
            c.drawCentredString(220, 520, 'QUANTITY')     
            c.drawCentredString(330, 520, 'UNIT PRICE')     
            c.drawCentredString(450, 520, 'LINE TOTAL')  


            c.setFont('Helvetica', 12, leading=None)
            c.drawCentredString(110, 490, line_one)     
            c.drawCentredString(220, 490, line_one_quantity)     
            c.drawCentredString(330, 490, line_one_unit_price)     
            c.drawCentredString(450, 490, line_one_total_price)     

            if line_two != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 460, line_two)     
                c.drawCentredString(220, 460, line_two_quantity)     
                c.drawCentredString(330, 460, line_two_unit_price)     
                c.drawCentredString(450, 460, line_two_total_price)     

            if line_three != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 430, line_three)     
                c.drawCentredString(220, 430, line_three_quantity)     
                c.drawCentredString(330, 430, line_three_unit_price)     
                c.drawCentredString(450, 430, line_three_total_price)     

            if line_four != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 400, line_four)     
                c.drawCentredString(220, 400, line_four_quantity)     
                c.drawCentredString(330, 400, line_four_unit_price)     
                c.drawCentredString(450, 400, line_four_total_price)     

            if line_five != '':
                c.setFont('Helvetica', 12, leading=None)
                c.drawCentredString(110, 370, line_five)     
                c.drawCentredString(220, 370, line_five_quantity)     
                c.drawCentredString(330, 370, line_five_unit_price)     
                c.drawCentredString(450, 370, line_five_total_price)          



            # TOTAL
            c.setFont('Helvetica-Bold', 20, leading=None)
            c.drawCentredString(400, 140, "TOTAL:")
            c.setFont('Helvetica-Bold', 20, leading=None)
            c.drawCentredString(484, 140, 'D'+total) 


            # SIGN
            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(150, 140, "Signed:__________________")
            c.setFont('Helvetica-Bold', 12, leading=None)
            c.drawCentredString(170, 120, 'Manager') 


            c.showPage()

            c.save()

        import_data(data_file)

    return render(request, 'list_invoice.html', context)

def add_invoice(request):
    
    form = InvoiceForm(request.POST or None)
    total_invoices = Invoice.objects.count()
    queryset = Invoice.objects.order_by('-invoice_date')[:7]
    
    if form.is_valid():
        form.save()
        return redirect("/list_invoice")
    context = {
        "form" : form,
        "title": "New Invoice",
        'total_invoices': total_invoices,
        'queryset' : queryset,
    }

    return render(request, "new_invoice.html", context)

    return render(request, "new_invoice.html", context)


def update_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    form = InvoiceUpdateForm(instance = queryset)
    if request.method == 'POST':
        form = InvoiceUpdateForm(request.POST, instance=queryset)
        
        if form.is_valid():
            form.save()
            return redirect("/list_invoice")

    context = {
        "form" : form,
    }

    return render(request, "new_invoice.html", context)



def delete_invoice(request, pk):
    queryset = Invoice.objects.get(id=pk)
    if request.method == 'POST':
        queryset.delete()
        return redirect("/list_invoice")
    return render(request, "delete_invoice.html")