# Generated by Django 5.0.12 on 2025-02-13 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GRN_Details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Location_DC', models.CharField(max_length=10)),
                ('Customer_Name', models.CharField(blank=True, max_length=255, null=True)),
                ('PO_Date', models.DateField()),
                ('PO_Number', models.CharField(max_length=50)),
                ('GRN_Date', models.DateField()),
                ('GRN_No', models.CharField(max_length=50)),
                ('Supplier_Doc_Date', models.DateField()),
                ('Suppliers_Doc_Ref', models.CharField(max_length=50)),
                ('Vehicle_Number', models.CharField(max_length=50)),
                ('Vendor_Name', models.CharField(max_length=255)),
                ('Unloading_end', models.CharField(blank=True, max_length=255, null=True)),
                ('Gate_In_Date', models.CharField(blank=True, max_length=255, null=True)),
                ('Data_from', models.CharField(max_length=50)),
                ('Item_Code', models.CharField(max_length=50)),
                ('Item_Desc', models.CharField(max_length=255)),
                ('GRN_Quantity', models.PositiveIntegerField()),
                ('Item_Category', models.CharField(max_length=255)),
                ('Item_Rate', models.DecimalField(decimal_places=3, max_digits=10)),
                ('Remaining_Qty', models.PositiveIntegerField()),
                ('Tax_Amount', models.DecimalField(decimal_places=4, max_digits=12)),
                ('Tax_Group', models.CharField(max_length=50)),
            ],
        ),
    ]
