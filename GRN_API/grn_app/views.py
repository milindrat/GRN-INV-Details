from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from datetime import datetime
import json
from .models import GRN_Details ,INV_Details

@csrf_exempt  # This is to allow POST requests from outside Django (avoid CSRF errors)
def create_grn_details(request):
    if request.method == 'POST':
        # Parse the incoming JSON data
        data = json.loads(request.body)
        
        # Convert string dates to Python date objects
        grn_date = datetime.strptime(data["GRN_Date"], "%d/%m/%Y").date()  # Adjusted date format
        po_date = datetime.strptime(data["PO_Date"], "%d/%m/%Y").date()    # Adjusted date format
        supplier_doc_date = datetime.strptime(data["Supplier_Doc_Date"], "%d/%m/%Y").date()  # Adjusted date format
        
        # Loop over the items and save them into the table
        for item in data["items"]:
            # Create a new GRN record with item details
            grn_entry = GRN_Details(
                Location_DC=data["Location_DC"],  # Location DC value
                Customer_Name=data["Customer_Name"],  
                PO_Date=po_date,
                PO_Number=data["PO_Number"],
                GRN_Date=grn_date,
                GRN_No=data["GRN_No"],
                Supplier_Doc_Date=supplier_doc_date,
                Suppliers_Doc_Ref=data["Suppliers_Doc_Ref"],
                Vehicle_Number=data["Vehicle_Number"],
                Vendor_Name=data["Vendor_Name"],
                Unloading_end=data["Unloading_end"],  # If None, return empty string
                Gate_In_Date=data["Gate_In_Date"],  # If None, return empty string
                Data_from=data["Data_from"],
                
                # Item details for this entry
                Item_Code=item["Item_Code"],
                Item_Desc=item["Item_Desc"],
                GRN_Quantity=item["GRN_Quantity"],
                Item_Category=item["Item_Category"],
                Item_Rate=item["Item_Rate"],
                Remaining_Qty=item["Remaining_Qty"],
                Tax_Amount=item["Tax_Amount"],
                Tax_Group=item["Tax_Group"]
            )
            # Save the GRN and item details to the database
            grn_entry.save()

        return JsonResponse({"message": "Data saved successfully!"}, status=201)

    return JsonResponse({"message": "Invalid request method."}, status=400)



@csrf_exempt  # This is to allow POST requests from outside Django (avoid CSRF errors)
def create_inv_details(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data
            data = json.loads(request.body)

            # Convert date from string to date object
            inv_date = datetime.strptime(data["Inv_date"], "%d/%m/%Y").date()

            # Loop through the items and save them in the database
            for item in data["items"]:
                # Create a new INV record
                inv_entry = INV_Details(
                    Customer=data["Customer"],
                    Location_DC=data["Location_DC"],
                    Store_code=data["Store_code"],
                    Store_name=data["Store_name"],
                    Store_State=data["Store_State"],
                    Store_Zone=data["Store_Zone"],
                    Inv_date=inv_date,
                    Invoice_number=data["Invoice_number"],
                    Total_Inv_amt=data["Total_Inv_amt"],
                    Document_type=data["Document_type"],
                    Created_from=data["Created_from"],
                    Shiping_addr=data["Shiping_addr"],
                    Billing_addr=data["Billing_addr"],
                    IRN_Details=data["IRN_Details"],  # Default to empty string if not provided
                    ERP_Type=data["ERP_Type"],
                    # Item details
                    Item_code=item["Item_code"],
                    Item_Desc=item["Item_Desc"],
                    Invoice_quantity=item["Invoice_quantity"],
                    Item_Category=item["Item_Category"],
                    Item_Rate=item["Item_Rate"],
                    Tax_code=item["Tax_code"]
                )

                # Save the record
                inv_entry.save()

            return JsonResponse({"message": "Data saved successfully!"}, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"message": "Invalid JSON format."}, status=400)
        except Exception as e:
            return JsonResponse({"message": str(e)}, status=500)

    return JsonResponse({"message": "Invalid request method."}, status=400)
