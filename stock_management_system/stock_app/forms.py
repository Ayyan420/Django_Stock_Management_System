from django import forms
from .models import Stock
from .models import StockListHistory
from .models import Categorie




# from here we will create stock


class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category','item_name','quantity','issue_by','date']
        # fields = '__all__'


        # validation
        # def clean_category(self):
        #     category = self.cleaned_data.get('category')
        #     if not category:
        #         raise forms.ValidationError("This field is required")
        #     for obj in Stock.objects.all():
        #         if obj.category == category:
        #             raise forms.ValidationError(category+" is already created")
        #     return category





        # def clean_item_name(self):
        #     # super(StockCreateForm, self).clean()
        #     item = self.cleaned_data.get('item_name')
        #     if not item:
        #         raise forms.ValidationError("This field is required")
        #     return item



# for search in list items




class StockSearchForm(forms.ModelForm):
    export_to_csv = forms.BooleanField(required=False)
    export_to_pdf = forms.BooleanField(required=False)
    class Meta:
        model = Stock
        fields = ['category','item_name']



class StockHistorySearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)
    export_to_csv = forms.BooleanField(required=False)
    export_to_pdf = forms.BooleanField(required=False)
    class Meta:
        model = StockListHistory
        fields = ['category','item_name','start_date','end_date']





class StockUpdateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['category','item_name','quantity','issue_by']







class IssueStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['issue_quantity','issue_to']



class ReceiveStockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['receive_quantity','receive_by']






class ReorderLevelForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['reorder_level']


class CreateCategory(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = ['name','created_by','upload_file','upload_img']
