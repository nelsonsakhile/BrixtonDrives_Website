from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
                'invoice_number',
                'invoice_date',
                'name',
                'phone_number',

                'line_one',
                'line_one_quantity',
                'line_one_unit_price',
                'line_one_total_price',

                'line_two',
                'line_two_quantity',
                'line_two_unit_price',
                'line_two_total_price',

                'line_three',
                'line_three_quantity',
                'line_three_unit_price',
                'line_three_total_price',

                'line_four',
                'line_four_quantity',
                'line_four_unit_price',
                'line_four_total_price',

                'line_five',
                'line_five_quantity',
                'line_five_unit_price',
                'line_five_total_price',

                'total',
                'deposit',
                'amount_due',
                'paid',
                'invoice_type',
                ]


        widgets = {
            'invoice_number' : forms.TextInput(attrs = {'class': 'form-control ' , 'required' : "required"}),
            'invoice_date' : forms.TextInput(attrs = {'class': 'form-control ','type': 'date', 'placeholder': 'YYYY-MM-DD'}),
            'name' : forms.TextInput(attrs = {'class': 'form-control' , 'required' : "required"}),
            'phone_number' : forms.TextInput(attrs = {'class': 'form-control'}),

            'line_one' : forms.TextInput(attrs = {'class': 'form-control', 'required' : "required"}),
            'line_one_quantity' : forms.TextInput(attrs = {'class': 'form-control'}),
            'line_one_unit_price' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_one_total_price' : forms.TextInput(attrs = {'class': 'form-control'}),

            'line_two' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_two_quantity' : forms.TextInput(attrs = {'class': 'form-control'}),
            'line_two_unit_price' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_two_total_price' : forms.TextInput(attrs = {'class': 'form-control'}),

            'line_three' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_three_quantity' : forms.TextInput(attrs = {'class': 'form-control'}),
            'line_three_unit_price' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_three_total_price' : forms.TextInput(attrs = {'class': 'form-control'}),

            'line_four' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_four_quantity' : forms.TextInput(attrs = {'class': 'form-control'}),
            'line_four_unit_price' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_four_total_price' : forms.TextInput(attrs = {'class': 'form-control'}),

            'line_five' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_five_quantity' : forms.TextInput(attrs = {'class': 'form-control'}),
            'line_five_unit_price' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_five_total_price' : forms.TextInput(attrs = {'class': 'form-control'}),

            'total' : forms.TextInput(attrs = {'class': 'form-control'}),
            'deposit' : forms.TextInput(attrs = {'class': 'form-control'}),
            'amount_due' : forms.TextInput(attrs = {'class': 'form-control'}),
            'paid' : forms.CheckboxInput(attrs = {'class': 'chekbox'}),
            'invoice_type' : forms.Select(attrs = {'class': 'form-control'}),
                }

class InvoiceSearchForm(forms.ModelForm):
    generate_invoice = forms.BooleanField(required=False)
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'name', 'generate_invoice',]

        widgets = {
                'invoice_number' : forms.TextInput(attrs = {'class': 'form-control '}),
                'name' : forms.TextInput(attrs = {'class': 'form-control'}),}


class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = [
                'invoice_number',
                'invoice_date',
                'name',
                'phone_number',

                'line_one',
                'line_one_quantity',
                'line_one_unit_price',
                'line_one_total_price',

                'line_two',
                'line_two_quantity',
                'line_two_unit_price',
                'line_two_total_price',

                'line_three',
                'line_three_quantity',
                'line_three_unit_price',
                'line_three_total_price',

                'line_four',
                'line_four_quantity',
                'line_four_unit_price',
                'line_four_total_price',

                'line_five',
                'line_five_quantity',
                'line_five_unit_price',
                'line_five_total_price',

                'total',
                'deposit',
                'amount_due',
                'paid',
                'invoice_type',
                ]
        widgets = {
            'invoice_number' : forms.TextInput(attrs = {'class': 'form-control ' , 'required' : "required"}),
            'invoice_date' : forms.TextInput(attrs = {'class': 'form-control ', 'type': 'date' ,'placeholder': 'YYYY-MM-DD'}),
            'name' : forms.TextInput(attrs = {'class': 'form-control' , 'required' : "required"}),
            'phone_number' : forms.TextInput(attrs = {'class': 'form-control'}),

            'line_one' : forms.TextInput(attrs = {'class': 'form-control', 'required' : "required"}),
            'line_one_quantity' : forms.TextInput(attrs = {'class': 'form-control'}),
            'line_one_unit_price' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_one_total_price' : forms.TextInput(attrs = {'class': 'form-control'}),

            'line_two' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_two_quantity' : forms.TextInput(attrs = {'class': 'form-control'}),
            'line_two_unit_price' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_two_total_price' : forms.TextInput(attrs = {'class': 'form-control'}),

            'line_three' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_three_quantity' : forms.TextInput(attrs = {'class': 'form-control'}),
            'line_three_unit_price' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_three_total_price' : forms.TextInput(attrs = {'class': 'form-control'}),

            'line_four' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_four_quantity' : forms.TextInput(attrs = {'class': 'form-control'}),
            'line_four_unit_price' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_four_total_price' : forms.TextInput(attrs = {'class': 'form-control'}),

            'line_five' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_five_quantity' : forms.TextInput(attrs = {'class': 'form-control'}),
            'line_five_unit_price' : forms.TextInput(attrs = {'class': 'form-control', }),
            'line_five_total_price' : forms.TextInput(attrs = {'class': 'form-control'}),

            'total' : forms.TextInput(attrs = {'class': 'form-control'}),
            'deposit' : forms.TextInput(attrs = {'class': 'form-control'}),
            'amount_due' : forms.TextInput(attrs = {'class': 'form-control'}),
            'paid' : forms.CheckboxInput(attrs = {'class': 'chekbox'}),
            'invoice_type' : forms.Select(attrs = {'class': 'form-control'}),
                }




class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']