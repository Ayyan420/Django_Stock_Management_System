from django.http import HttpResponse
import csv
from django.template import loader
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect 

from django.utils import timezone

from stock_app.models import *
from stock_app.forms import *
import datetime


# decorators


from django.contrib.auth.decorators import login_required


# for pdf




import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape


from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


# foe email



from django.conf import settings
from django.core.mail import send_mail





pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

pdfmetrics.registerFont(TTFont('DejaVuSans','DejaVuSans.ttf'))





from django.contrib import messages

# @login_required
# def home(request):
#     return redirect('/list_items')

@login_required
@csrf_exempt
def list_items(request):
    form = StockSearchForm(request.POST or None) 
    query_set = Stock.objects.all().order_by('-quantity')
    context = {
    'query_set':query_set,
    'form':form,
    }
    

    # this will return rewsults and give us results with qury
    if request.method == "POST":
        # code to export to csv
        # query_set = Stock.objects.filter(category__id__icontains = form['category'].value(),item_name__icontains = form['item_name'].value())
        

        query_set = Stock.objects.filter(category__id__icontains = form['category'].value(),item_name__icontains = form['item_name'].value())
        # category__id__icontains for foreign key


        if form['export_to_csv'].value()==True and form['export_to_pdf'].value()==False:
            response = HttpResponse(content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename="List Of Items.csv"'
            writer = csv.writer(response)
            writer.writerow(['Category','Item Name','Quantity'])
            obj = query_set
            for stock in obj:
                writer.writerow([stock.category,stock.item_name,stock.quantity])
            return response




        if form['export_to_csv'].value()==False and form['export_to_pdf'].value()==True:
              # Create a file-like buffer to receive PDF data.
            buffer = io.BytesIO()

            # Create the PDF object, using the buffer as its "file."
            p = canvas.Canvas(buffer)
            p.setFont("Times-Bold", 15)
            p.setFillColorRGB(0, 0, 0)
            p.getPageNumber() 


            # Draw things on the PDF. Here's where the PDF generation happens.

            obj = query_set
            width_left = 40
            width_left2 = 220
            width_left3 = 340
            width_left4 = 430
            height_top = 650

            p.drawString(250, 750,"LIST OF ITEMS")
            for stock in obj:
                data = "Category : {} ".format(stock.category)
                data1 = "Item : {} ".format(stock.item_name)
                data2 = "Qty : {} ".format(stock.quantity)
                data3 = "Reorder Level : {} ".format(stock.reorder_level)
                p.drawString(width_left, height_top,data)
                p.drawString(width_left2, height_top,data1)
                p.drawString(width_left3, height_top,data2)
                p.drawString(width_left4, height_top,data3)
                height_top-=30


            # Close the PDF object cleanly, and we're done.
            p.showPage()
            p.save()

            # FileResponse sets the Content-Disposition header so that browsers
            # present the option to save the file.

            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename='List Of Items.pdf')

        if form['export_to_csv'].value()==True and form['export_to_pdf'].value()==True:
            messages.success(request, "Please select one option at a time!")
            

        context = {
        'form':form,
        'query_set':query_set,
        }

    return render(request,"stock_app/main/list_items.html",context)

@login_required
@csrf_exempt
def add_items(request):
    # before saving it will check is it validated
    # form = StockCreateForm(request.POST or None)
    if request.method == "POST":
        form = StockCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/list_items")
                    # raise forms.ValidationError(category+" is already created")
        else:
            return redirect("/")
    else:
        form = StockCreateForm()

    context = {
    'form':form,
    }

    return render(request,"stock_app/main/add_items.html",context)

@login_required
@csrf_exempt
def update_items(request,id_get):
    query_set = Stock.objects.get(id=id_get)
    if request.method == "POST":
        form = StockUpdateForm(request.POST, instance=query_set)
        if form.is_valid():
            form.save()
            return redirect("/list_items")
        else:
            return redirect("/")
    else:
        form = StockCreateForm(instance=query_set)

    context = {
    'form':form,
    }

    return render(request,"stock_app/main/add_items.html",context)

@login_required
@csrf_exempt
def del_items(request,id_get):
    query_set = Stock.objects.get(id=id_get).delete()
    messages.success(request,'Successfully deleted!')
    return HttpResponseRedirect('/list_items')




def stock_detail(request,id_pk):
    
    query = Stock.objects.get(id=id_pk)
    context = {
    'query':query
    }
    return render(request,"stock_app/main/stock_detail.html",context)




@login_required
@csrf_exempt
def issue_items(request,id_pk):
    query_set = Stock.objects.get(id=id_pk)
    if request.method == "POST":
        form = IssueStockForm(request.POST, instance=query_set)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.quantity -= instance.issue_quantity
            instance.issue_by = str(request.user.get_username())

            qty = instance.quantity
            messages.success(request, "Issued Successfully:  " + str(instance.quantity)+ " " + str(instance.item_name)+"s now left in Store")
            
            instance.receive_quantity=0

            query_set_history = StockListHistory.objects.create(category = instance.category, item_name=instance.item_name,issue_quantity=instance.issue_quantity,receive_quantity=0,quantity=instance.quantity,last_update=instance.last_update, issue_by = str(request.user) , receive_by = None)
            
            instance.save()
            
            return redirect("/stock_detail/"+ str(instance.id))
        else:
            return redirect("/list_items")
    else:
        form = IssueStockForm(instance=query_set)

    context = {
    'title': 'Issue '+ str(query_set.item_name),
    'form':form,
    'query_set':query_set,
    'username':'Issue By '+ str(request.user.get_username()),
    }

    return render(request,"stock_app/main/issue_items.html",context)


@login_required
@csrf_exempt
def receive_items(request,id_pk):
    query_set = Stock.objects.get(id=id_pk)
    if request.method == "POST":
        form = ReceiveStockForm(request.POST, instance=query_set)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.quantity += int(instance.receive_quantity)

            instance.receive_by = str(request.user.get_username())
            messages.success(request, "Received Successfully:  " + str(instance.quantity)+ " " + str(instance.item_name)+"s are now in Store")

            instance.issue_quantity=0

            query_set_history = StockListHistory.objects.create(category = instance.category, item_name=instance.item_name,issue_quantity=0,receive_quantity=instance.receive_quantity,quantity=instance.quantity,last_update=instance.last_update, issue_by = None , receive_by = str(request.user))


            instance.save()
            return redirect("/stock_detail/"+ str(instance.id))
        else:
            return redirect("/list_items")
    else:
        form = ReceiveStockForm(instance=query_set)

    context = {
    'title': 'Receive '+ str(query_set.item_name),
    'form':form,
    'query_set':query_set,
    'username':'Receive By '+ str(request.user.get_username()),
    }

    return render(request,"stock_app/main/receive_items.html",context)




@login_required
@csrf_exempt
def reorder_items(request,id_pk):
    query_set = Stock.objects.get(id=id_pk)
    color=""
    if request.method == "POST":
        form = ReorderLevelForm(request.POST, instance=query_set)
        if form.is_valid():
            instance = form.save(commit=False)
            query_set.reorder_level = int(instance.reorder_level)
            messages.success(request, "Reorder Level For {} Changed Successfully:  ".format(instance.item_name))
            instance.save()

            return redirect("/list_items")
        
        else:
            return redirect("/list_items")
    else:
        form = ReorderLevelForm(instance=query_set)

    context = {
    'form':form,
    'query_set':query_set,
    }

    return render(request,"stock_app/main/reorder_items.html",context)





@login_required
@csrf_exempt

def list_history(request):

    form = StockHistorySearchForm(request.POST or None)


    


    query_set = StockListHistory.objects.all().order_by('-quantity')
    context = {
    'query_set':query_set,
    'form':form,
    }



     # this will return rewsults and give us results with qury
    if request.method == "POST":
        # code to export to csv
        # query_set = Stock.objects.filter(category__id__icontains = form['category'].value(),item_name__icontains = form['item_name'].value())

        if (form['start_date'].value() and form['end_date'].value()):
            query_set = StockListHistory.objects.filter(category__id__icontains = form['category'].value(),item_name__icontains = form['item_name'].value(), last_update__range=[form['start_date'].value(),
                form['end_date'].value()
                ])

        
        elif (form['category'].value()) or (form['item_name'].value()):
            query_set = StockListHistory.objects.filter(category__id__icontains = form['category'].value(),item_name__icontains = form['item_name'].value())


        elif form['export_to_csv'].value()==True and form['export_to_pdf'].value()==False:
            response = HttpResponse(content_type="text/csv")
            response['Content-Disposition'] = 'attachment; filename="List History Of Items.csv"'
            writer = csv.writer(response)
            writer.writerow(['Category','Item Name','Quantity','Issue Quantity','Issue By','Receive Quantity','Receive By'])
            obj = query_set
            for stock in obj:
                writer.writerow([stock.category,stock.item_name,stock.quantity,stock.issue_quantity,stock.issue_by,stock.receive_quantity,stock.receive_by])
            return response




        elif form['export_to_csv'].value()==False and form['export_to_pdf'].value()==True:
              # Create a file-like buffer to receive PDF data.
            buffer = io.BytesIO()

            # Create the PDF object, using the buffer as its "file."
            p = canvas.Canvas(buffer, pagesize=landscape(letter))
            # c = canvas.Canvas(file, pagesize=landscape(letter))

            p.setFont("DejaVuSans", 11)
            p.setFillColorRGB(0, 0, 0)
            p.getPageNumber() 


            # Draw things on the PDF. Here's where the PDF generation happens.

            obj = query_set
            width_left = 20
            width_left1 = 160
            width_left2 = 260
            width_left3 = 340
            width_left4 = 430
            width_left5 = 540
            width_left6 = 670
            height_top = 470

            p.drawString(350, 550,"LIST HISTORY")
            for stock in obj:
                data = "Category : {} ".format(stock.category)
                data1 = "Item : {} ".format(stock.item_name)
                data2 = "Qty : {} ".format(stock.quantity)
                data3 = "Issue Qty : {} ".format(stock.issue_quantity)
                data4 = "Issue By : {} ".format(stock.issue_by)
                data5 = "Receive Qty : {} ".format(stock.receive_quantity)
                data6 = "Receive By : {} ".format(stock.receive_by)
                p.drawString(width_left, height_top,data)
                p.drawString(width_left1, height_top,data1)
                p.drawString(width_left2, height_top,data2)
                p.drawString(width_left3, height_top,data3)
                p.drawString(width_left4, height_top,data4)
                p.drawString(width_left5, height_top,data5)
                p.drawString(width_left6, height_top,data6)
                height_top-=30


            # Close the PDF object cleanly, and we're done.
            p.showPage()
            p.save()


            buffer.seek(0)
            return FileResponse(buffer, as_attachment=True, filename='List History Of Items.pdf')

        elif form['export_to_csv'].value()==True and form['export_to_pdf'].value()==True:
            messages.success(request, "Please select one option at a time!")


        elif not (form['start_date'].value() and form['end_date'].value()):
            messages.success(request, "Please Add Both Dates!")
            query_set = StockListHistory.objects.filter()
            

        context = {
        'form':form,
        'query_set':query_set,
        }

    
    return render(request,"stock_app/main/list_history.html",context)














@login_required
@csrf_exempt
def create_category(request):
    all_category = Categorie.objects.all()

    cate_names = []
    for x in all_category:
        cate_names.append(x.name)

    
    if request.method == "POST":
        form = CreateCategory(request.POST, request.FILES)
        if form.is_valid():
            if not form['name'].value() in cate_names:
                form.save()
                return redirect("/create_category")

            else:
                name = str(form['name'].value())
                messages.success(request, "Category %s is Already Present!"%name)
                return redirect("/list_items")


    else:
        form = CreateCategory() 

    context = {
    'form':form,
    'all_category':all_category,
    }

    return render(request,"stock_app/main/create_category.html",context)













@login_required
@csrf_exempt
def del_categories(request,id_get):
    query_set = Categorie.objects.get(id=id_get)
    messages.success(request,'Category Successfully deleted!')
    query_set.delete()
    return HttpResponseRedirect('/create_category')







# upload file using model


# from django.core.files.storage import FileSystemStorage
# # import model
# def upload(request):
#     if request.method=="POST" and request.FILES["my_input_file_id"]:
#         my_input_file = request.FILES["my_input_file_id"]

#         fs = FileSystemStorage()

#         filename = fs.save(my_input_file.name, my_input_file)
#         url = fs.url(filename)
#         new_profile = model(image = url)
#         new_profile.save()
#         redirect()


def send_e_mail(request):
    return render(request,"stock_app/main/send_mail.html")


@csrf_exempt
def send_ee_mail(request):
    if request.method=="POST":
        subject =  request.POST['subject']
        message =  request.POST['message']
        email_from = settings.EMAIL_HOST_USER
        email_to = request.POST['email_to']


        print(subject)
        print(message)
        print(email_from)
        print(email_to)
        # recipient_list = ['ayyansaddiqui420@gmail.com']
        recipient_list = ['%s'%email_to]
        send_mail( subject, message, email_from, recipient_list )

        messages.success(request,"Successfully Send Mail To %s ."%email_to )
        return redirect('/')
    else:
        messages.success(request,"Mail Sending Is Failed To  %s ."%email_to )
        return redirect('/')