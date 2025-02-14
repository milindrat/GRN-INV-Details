from django.db import models

# Create your models here.

class GRN_Details(models.Model):
    Location_DC = models.CharField(max_length=10)
    Customer_Name = models.CharField(max_length=255, null=True, blank=True)
    PO_Date = models.DateField()
    PO_Number = models.CharField(max_length=50)
    GRN_Date = models.DateField()
    GRN_No = models.CharField(max_length=50)
    Supplier_Doc_Date = models.DateField()
    Suppliers_Doc_Ref = models.CharField(max_length=50)
    Vehicle_Number= models.CharField(max_length=50)
    Vendor_Name= models.CharField(max_length=255)
    Unloading_end= models.CharField(max_length=255, null=True, blank=True)
    Gate_In_Date = models.CharField(max_length=255, null=True, blank=True)
    Data_from = models.CharField(max_length=50)

    Item_Code = models.CharField(max_length=50)
    Item_Desc = models.CharField(max_length=255)
    GRN_Quantity = models.PositiveIntegerField()
    Item_Category = models.CharField(max_length=255)
    Item_Rate = models.DecimalField(max_digits=10, decimal_places=3)
    Remaining_Qty = models.PositiveIntegerField()
    Tax_Amount= models.DecimalField(max_digits=12, decimal_places=4)
    Tax_Group = models.CharField(max_length=50)


class INV_Details(models.Model):
    Customer = models.CharField(max_length=255)
    Location_DC = models.CharField(max_length=255)
    Store_code = models.CharField(max_length=50)
    Store_name = models.CharField(max_length=255)
    Store_State = models.CharField(max_length=255)
    Store_Zone = models.CharField(max_length=255)
    Inv_date = models.DateField()
    Invoice_number = models.CharField(max_length=50)
    Total_Inv_amt = models.DecimalField(max_digits=12, decimal_places=2)
    Document_type = models.CharField(max_length=50)
    Created_from = models.CharField(max_length=50)
    Shiping_addr = models.TextField()
    Billing_addr = models.TextField()
    IRN_Details = models.TextField(blank=True, null=True)
    ERP_Type = models.CharField(max_length=50)

    Item_code = models.CharField(max_length=50)
    Item_Desc = models.CharField(max_length=255)
    Invoice_quantity = models.PositiveIntegerField()
    Item_Category = models.CharField(max_length=50)
    Item_Rate = models.DecimalField(max_digits=10, decimal_places=3)
    Tax_code = models.CharField(max_length=50)

   
