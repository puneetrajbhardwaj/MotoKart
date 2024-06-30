"""motokart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from motokart import StateCityView


from . import CategoryView
from . import SubCategoryView
from . import ProductView
from . import ChatBotView
from . import CustomerView
from . import EmployeeView

urlpatterns = [
    path('admin/clearcache/', include('clearcache.urls')),
    path('admin/', admin.site.urls),
    #Category
    path('categoryinterface/',CategoryView.CategoryInterface),
    path('categorysubmit',CategoryView.CategorySubmit),
    path('displaycategories/',CategoryView.DisplayCategories),
    path('getcategoriesjson/',CategoryView.GetCategoryJSON),
    path('displaycategoriesemployee/',CategoryView.DisplayCategoriesEmployee),
    path('displaycategorybyid/',CategoryView.DisplayCategoryById),
    path('editdeletecategory/',CategoryView.EditDeleteCategory),
    path('editcategoryicon/',CategoryView.EditCategoryIcon),
    path('saveeditcategoryicon',CategoryView.SaveEditCategoryIcon),

    #SubCategory
    path('subcategoryinterface/',SubCategoryView.SubCategoryInterface),
    path('subcategorysubmit',SubCategoryView.SubCategorySubmit),
    path('displaysubcategories/',SubCategoryView.DisplaySubCategories),
    path('getsubcategoriesjson/',SubCategoryView.GetSubCategoryJSON),
    path('displaysubcategoriesemployee/',SubCategoryView.DisplaySubCategoriesEmployee),
    path('displaysubcategorybyid/',SubCategoryView.DisplaySubcategoryById),
    path('editdeletesubcategory/',SubCategoryView.EditDeleteSubCategory),
    path('editsubcategoryicon/',SubCategoryView.EditSubCategoryIcon),
    path('saveeditsubcategoryicon',SubCategoryView.SaveEditSubCategoryIcon),
    path('displayallsubcategoriesemployee/',SubCategoryView.DisplayAllSubCategoriesEmployee),

    #Product
    path('productinterface/',ProductView.ProductInterface),
    path('productsubmit',ProductView.ProductSubmit),
    path('displayproducts/',ProductView.DisplayProducts),
    path('bill/',ProductView.Bill),
    path('printbill/',ProductView.PrintBill),
    path('getproductjson/',ProductView.GetProductJSON),
    path('displayproductsemployee/',ProductView.DisplayProductsEmployee),
    path('displayproductbyid/',ProductView.DisplayProductById),
    path('editdeleteproduct/',ProductView.EditDeleteProduct),
    path('editproducticon/',ProductView.EditProductIcon),
    path('saveeditproducticon',ProductView.SaveEditProductIcon),
    path('displayallproductsemployee/',ProductView.DisplayAllProductsEmployee),
    path('selectforcomparision/',ProductView.SelectForComparison),
    path('showcomparison/',ProductView.ShowComparison),

    #Customers
    path('customerhomepage/',CustomerView.CustomerHomepage),
    path('customerloginregister/',CustomerView.CustomerLoginRegister),
    path('customerregistration',CustomerView.CustomerRegistration),
    path('submitcustomer',CustomerView.SubmitCustomer),
    path('getusernamejson/',CustomerView.GetUsernameJSON),
    path('customerupdateusernamepassword/', CustomerView.CustomerUpdateUsernamePassword),
    path('customerupdateusername',CustomerView.CustomerUpdateUsername),
    path('customerupdatepassword',CustomerView.CustomerUpdatePassword),
    # path('customerlogin/',CustomerView.CustomerLogin),
    path('checkcustomerlogin',CustomerView.CheckCustomerLogin),
    path('customerlogout/',CustomerView.CustomerLogout),
    path('customersearch/',CustomerView.CustomerSearch),
    path('customerloginoptions/',CustomerView.CustomerLoginOptions),
    path('customereditprofile/',CustomerView.CustomerEditProfile),
    path('customerupdate/',CustomerView.CustomerUpdate),
    path('customerprofile/',CustomerView.CustomerProfile),
    path('paymentpage/',CustomerView.PaymentPage),
    path('addtowishlist/',CustomerView.AddToWishlist),
    path('showwishlist/',CustomerView.ShowWishlist),
    path('removefromwishlist/',CustomerView.RemoveFromWishlist),

    #Employee
    path('employeelogin/',EmployeeView.EmployeeLogin),
    path('checkemployeelogin',EmployeeView.CheckEmployeeLogin),
    path('employeelogout/',EmployeeView.EmployeeLogout),
    path('employeesearch/',EmployeeView.EmployeeSearch),
    
 
    #Chatbot
    path('showchat/',ChatBotView.ShowChat),
    path('chatbot/',ChatBotView.ChatBot),

    #StateCity
    path('fetchallstates/',StateCityView.FetchAllStates),
    path('fetchallcities/',StateCityView.FetchAllCities),
]
