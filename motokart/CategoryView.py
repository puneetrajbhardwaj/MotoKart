from django.shortcuts import render
from . import Pool
import uuid
import os
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin

location="D:/study/wipro internship/project/data/Motokart/motokart/assets/images/"
#Form Used to insert categories.
@xframe_options_sameorigin
def CategoryInterface(request):
    try:
        result=request.session['EMPLOYEE']
        return render(request,"CategoryInterface.html")
    except Exception as e:
        print('erorr:',e)
        return render(request,"EmployeeLogin.html")    

#Saving the categories to the server
@xframe_options_sameorigin
def CategorySubmit(request):
    try:
        result=request.session['EMPLOYEE']
        try:
            categoryname=request.POST['categoryname']
            icon=request.FILES['categoryicon']
            cdescription=request.POST['cdescription']
            categoryicon=str(uuid.uuid4())+icon.name[icon.name.rfind('.'):]
            q="insert into categories(categoryname,cdescription,categoryicon)values('{}','{}','{}')".format(categoryname,cdescription,categoryicon)
            db,cmd=Pool.ConnectionPool()
            cmd.execute(q)
            db.commit()
            F=open(location+categoryicon,"wb")
            for chunk in icon.chunks():
                F.write(chunk)
            F.close()
            db.close()
            return render(request,"CategoryInterface.html",{'msg':'Record submitted Successfully'})
        except Exception as e:
            print('error',e)
            return render(request,"CategoryInterface.html",{'msg':'Record submition failed'})
    except Exception as e:
        print('erorr:',e)
        return render(request,"EmployeeLogin.html")

#Used to Display the categories for customer
@xframe_options_sameorigin
def DisplayCategories(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from categories"
        cmd.execute(q)
        rows=cmd.fetchall()
        return render(request,'DisplayCategories.html',{'rows':rows})
    except Exception as e:
        print('error',e)
        return render(request,'DisplayCategories.html', {'rows':[]})    

#Get categories to the user side in JSON format
@xframe_options_sameorigin        
def GetCategoryJSON(request):
    try:
        
        db,cmd=Pool.ConnectionPool()
        q="select * from categories"
        cmd.execute(q)
        rows=cmd.fetchall()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print('error',e)
        return JsonResponse(rows,safe=False)    

#Used to display the categories to Employee
@xframe_options_sameorigin
def DisplayCategoriesEmployee(request):
    try:
        result=request.session['EMPLOYEE']
        db,cmd=Pool.ConnectionPool()
        q="select * from categories"
        cmd.execute(q)
        rows=cmd.fetchall()
        return render(request,'DisplayCategoriesEmployee.html',{'rows':rows})
    except Exception as e:
        print('error',e)
        return render(request,"EmployeeLogin.html")             

#Form to edit the categories
@xframe_options_sameorigin
def DisplayCategoryById(request):
    categoryid=request.GET['categoryid']
    try:
        result=request.session['EMPLOYEE']
        db, cmd = Pool.ConnectionPool()
        q = "select * from categories where categoryid={}".format(categoryid)
        cmd.execute(q)
        row = cmd.fetchone()
        return render(request,'DisplayCategoryById.html', {'row': row})
    except Exception as e:
        print('error', e)
        return render(request,"EmployeeLogin.html")   
        
#Used to edit and delete the category        
@xframe_options_sameorigin
def EditDeleteCategory(request):
    try:
        result=request.session['EMPLOYEE']
        btn=request.GET['btn']
        categoryid=request.GET["categoryid"]
        categoryicon=request.GET["categoryicon"]
        print("xxxxxxxxxxxx",btn)
        if(btn=="Edit"):
            categoryname=request.GET['categoryname']
            cdescription=request.GET['cdescription']
            try:
                db, cmd = Pool.ConnectionPool()
                q = "update categories set categoryname='{}',cdescription='{}' where categoryid={}".format(categoryname,cdescription,categoryid)
                print (q)
                cmd.execute(q)
                db.commit()
                db.close()
                return DisplayCategoriesEmployee(request)
            except Exception as e:
                print("Error:", e)
                return DisplayCategoriesEmployee(request)

        elif (btn=="Delete"):

            try:
                db, cmd = Pool.ConnectionPool()
                os.remove(location+categoryicon)
                q="SELECT producticon FROM products where categoryid={}".format(categoryid)
                cmd.execute(q)
                rows=cmd.fetchall()
                for i in rows:
                    os.remove(location+i[0])
                q = "delete from products where categoryid={}".format(categoryid)
                print(q)
                cmd.execute(q)
                q="SELECT subcategoryicon FROM subcategories where categoryid={}".format(categoryid)
                cmd.execute(q)
                rows=cmd.fetchall()
                for i in rows:
                    os.remove(location+i[0])
                q = "delete from subcategories where categoryid={}".format(categoryid)
                cmd.execute(q)    
                print(q)
                q = "delete from categories where categoryid={}".format(categoryid)
                print(q)
                cmd.execute(q)
                db.commit()
                db.close()
                return DisplayCategoriesEmployee(request)
            except Exception as e:
                print(e)
                return DisplayCategoriesEmployee(request)
    except Exception as e:
        print('error', e)
        return render(request,"EmployeeLogin.html") 

#Change the category icon
@xframe_options_sameorigin
def EditCategoryIcon(request):
    try:
        result=request.session['EMPLOYEE']
        try:
            categoryid=request.GET['categoryid']
            categoryname=request.GET['categoryname']
            categoryicon=request.GET['categoryicon']
            row=[categoryid,categoryname,categoryicon]
            return render(request,"EditCategoryIcon.html",{'row':row})
        except Exception as e:
            print('error:',e)
            return render(request,"EditCategoryIcon.html",{'row':[]})    
    except Exception as e:
        print('error', e)
        return render(request,"EmployeeLogin.html")

#Uplod the categoryicon to the server
@xframe_options_sameorigin
def SaveEditCategoryIcon(request):
    try:
        result=request.session['EMPLOYEE']
        try:
            categoryid=request.POST['categoryid']
            oldpicture=request.POST['oldicon']
            picture=request.FILES['categoryicon']
            filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
            q="update categories set categoryicon='{}' where categoryid={}".format(filename,categoryid)
            print(q)
            db,cmd=Pool.ConnectionPool()
            cmd.execute(q)
            db.commit()
            F=open(location+filename,"wb")
            for chunk in picture.chunks():
                F.write(chunk)
            F.close()
            db.close()
            os.remove(location+oldpicture)
            return DisplayCategoriesEmployee(request)
        except Exception as e:
            print("Error:", e)
            return DisplayCategoriesEmployee(request)  

    except Exception as e:
        print('error', e)
        return render(request,"EmployeeLogin.html")
     
              