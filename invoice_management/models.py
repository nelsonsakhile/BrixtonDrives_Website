from django.db import models


# Create your models here.

class Invoice(models.Model):
    comments = models.CharField(max_length=3000, default='', null=True)
    invoice_number = models.IntegerField(blank=True, null=True)
    invoice_date = models.DateField(auto_now_add=False, auto_now=False, null=True)
    name = models.CharField('Customer name', max_length=120, default='', blank=True, null=True)
    phone_number = models.CharField(max_length=120, default='', blank=True, null=True)

    line_one = models.CharField("Item 1", max_length=120, default='', blank=True, null=True)
    line_one_quantity = models.IntegerField('Quantity', default='', blank=True, null=True)
    line_one_unit_price = models.IntegerField("Unit Price (R)", default=0, blank=True, null=True)
    line_one_total_price = models.IntegerField("Line total (R)", default=0, blank=True, null=True)
    
    line_two = models.CharField("Item 2", max_length=120, default='', blank=True, null=True)
    line_two_quantity = models.IntegerField('Quantity', default='', blank=True, null=True)
    line_two_unit_price = models.IntegerField("Unit Price (R)", default=0, blank=True, null=True)
    line_two_total_price = models.IntegerField("Line total (R)", default=0, blank=True, null=True)

    line_three = models.CharField("Item 3", max_length=120, default='', blank=True, null=True)
    line_three_quantity = models.IntegerField('Quantity', default='', blank=True, null=True)
    line_three_unit_price = models.IntegerField("Unit Price (R)", default=0, blank=True, null=True)
    line_three_total_price = models.IntegerField("Line total (R)", default=0, blank=True, null=True)

    line_four = models.CharField("Item 4", max_length=120, default='', blank=True, null=True)
    line_four_quantity = models.IntegerField('Quantity', default='', blank=True, null=True)
    line_four_unit_price = models.IntegerField("Unit Price (R)", default=0, blank=True, null=True)
    line_four_total_price = models.IntegerField("Line total (R)", default=0, blank=True, null=True)

    line_five = models.CharField("Item 5", max_length=120, default='', blank=True, null=True)
    line_five_quantity = models.IntegerField('Quantity', default='', blank=True, null=True)
    line_five_unit_price = models.IntegerField("Unit Price (R)", default=0, blank=True, null=True)
    line_five_total_price = models.IntegerField("Line total (R)", default=0, blank=True, null=True)

    
    total = models.IntegerField('Total (R)',default='0', blank=True, null=True)
    deposit = models.IntegerField('Deposit (R)',default='0', blank=True, null=True)
    amount_due = models.IntegerField('Amount Due (R)',default='0', blank=True, null=True)
    timestamp = models.DateField(auto_now_add=False, auto_now=False, null=True)
    last_updated = models.DateField(auto_now_add=False, auto_now=False, null=True)
    paid = models.BooleanField(default=False)
    invoice_type_choice = (
        ('Receipt', 'Receipt'),
        ('Invoice', 'Invoice')
    )
    invoice_type = models.CharField(max_length=50, default='', blank=True, null=True, choices=invoice_type_choice)

    def __str__(self):
        return f"{self.name}  | {self.invoice_number}  |  {self.invoice_type} | {self.invoice_date}"





'''

'''