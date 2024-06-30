from unicodedata import category
from unittest import result
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render

from motokart.EmployeeView import EmployeeLogin
from . import Pool
import uuid
import os
from django.views.decorators.clickjacking import xframe_options_sameorigin

location="D:/study/wipro internship/project/data/Motokart/motokart/assets/images/"
@xframe_options_sameorigin
def SubCategoryInterface(request):
    try:
        result=request.session['EMPLOYEE']
        return render(request,"SubcategoryInterface.html")
    except Exception as e:
        print('error@17',e)
        return EmployeeLogin(request)    

@xframe_options_sameorigin
def SubCategorySubmit(request):
    try:
        result=request.session['EMPLOYEE']
        try:
            categoryid=request.POST['categoryid']
            subcategoryname=request.POST['subcategoryname']
            scdescription=request.POST['scdescription']
            icon=request.FILES['subcategoryicon']
            subcategoryicon=str(uuid.uuid4())+icon.name[icon.name.rfind('.'):]
            q="insert into subcategories(categoryid,subcategoryname,scdescription,subcategoryicon)values({},'{}','{}','{}')".format(categoryid,subcategoryname,scdescription,subcategoryicon)
            db,cmd=Pool.ConnectionPool()
            cmd.execute(q)
            db.commit()
            F=open(location+subcategoryicon,"wb")
            for chunk in icon.chunks():
                F.write(chunk)
            F.close()
            db.close()
            return render(request,"SubcategoryInterface.html",{'msg':'Record submitted Successfully'})
        except Exception as e:
            print('error',e)
            return render(request,"SubcategoryInterface.html",{'msg':'Record submition failed'})
    except Exception as e:
        print('error@47:',e)
        return EmployeeLogin(request)


@xframe_options_sameorigin
def DisplaySubCategories(request):
    try:
        categoryid=request.GET['categoryid']
        db,cmd=Pool.ConnectionPool()
        q="select S.* ,(select C.categoryname from categories C where C.categoryid=S.categoryid) from subcategories S where S.categoryid={}".format(categoryid)
        cmd.execute(q)
        rows=cmd.fetchall()
        return render(request,'DisplaySubCategories.html',{'rows':rows})
    except Exception as e:
        print('error',e)
        return render(request,'DisplaySubCategories.html', {'rows':[]})

@xframe_options_sameorigin
def GetSubCategoryJSON(request):
    try:
        db,cmd=Pool.ConnectionPool()
        categoryid=request.GET['categoryid']
        q="select * from subcategories where categoryid={}".format(categoryid)
        print(q)
        cmd.execute(q)
        rows=cmd.fetchall()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print('error',e)
        return JsonResponse(rows,safe=False)

@xframe_options_sameorigin
def DisplaySubCategoriesEmployee(request):
    try:
        result=request.session['EMPLOYEE']
        db,cmd=Pool.ConnectionPool()
        categoryid=request.GET['categoryid']
        q="select * from subcategories where categoryid={}".format(categoryid)
        cmd.execute(q)
        rows=cmd.fetchall()
        return render(request,'DisplaySubCategoriesEmployee.html',{'rows':rows})
    except Exception as e:
        print('error',e)
        return EmployeeLogin(request)   

@xframe_options_sameorigin
def DisplaySubcategoryById(request):
    subcategoryid=request.GET['subcategoryid']
    try:
        result=request.session['EMPLOYEE']
        db, cmd = Pool.ConnectionPool()
        q = "select S.* ,C.categoryname from subcategories S, categories C where C.categoryid=S.categoryid and S.subcategoryid={}".format(subcategoryid)
        cmd.execute(q)
        row = cmd.fetchone()
        return render(request,'DisplaySubCategoryById.html', {'row': row})
    except Exception as e:
        print('error', e)
        return EmployeeLogin(request)   

@xframe_options_sameorigin
def EditDeleteSubCategory(request):
    try:
        result=request.session['EMPLOYEE']
        btn=request.GET['btn']
        subcategoryid=request.GET["subcategoryid"]
        print('subcategoryid:',subcategoryid)
        subcategoryicon=request.GET["subcategoryicon"]
        print("xxxxxxxxxxxx",btn)
        if(btn=="Edit"):
            categoryid=request.GET['categoryid']
            subcategoryname=request.GET['subcategoryname']
            scdescription=request.GET['scdescription']
            try:
                db, cmd = Pool.ConnectionPool()
                q = "update subcategories set categoryid={}, subcategoryname='{}' , scdescription='{}' where subcategoryid={}".format(categoryid,subcategoryname,scdescription,subcategoryid)
                print (q)
                cmd.execute(q)
                db.commit()
                db.close()
                return DisplaySubCategoriesEmployee(request)
            except Exception as e:
                print("Error:", e)
                return DisplaySubCategoriesEmployee(request)

        elif (btn=="Delete"):

            try:
                os.remove(location+subcategoryicon)
                db, cmd = Pool.ConnectionPool()
                q="SELECT producticon FROM products where subcategoryid={}".format(subcategoryid)
                cmd.execute(q)
                rows=cmd.fetchall()
                for i in rows:
                    os.remove(location+i[0])
                q = "delete from products where subcategoryid={}".format(subcategoryid)
                cmd.execute(q)
                q = "delete from subcategories where subcategoryid={}".format(subcategoryid)
                cmd.execute(q)
                db.commit()
                db.close()
                return DisplaySubCategoriesEmployee(request)
            except Exception as e:
                print(e)
                return DisplayAllSubCategoriesEmployee(request)  
    except Exception as e:
        print('error@151:',e)
        return EmployeeLogin(request)                      

@xframe_options_sameorigin
def EditSubCategoryIcon(request):
    try:
        result=request.session['EMPLOYEE']
        categoryid=request.GET['categoryid']
        subcategoryid=request.GET['subcategoryid']
        subcategoryname=request.GET['subcategoryname']
        subcategoryicon=request.GET['subcategoryicon']
        row=[subcategoryid,subcategoryname,subcategoryicon,categoryid]
        return render(request,"EditSubCategoryIcon.html",{'row':row})
    except Exception as e:
        print('error:',e)
        return EmployeeLogin(request)

@xframe_options_sameorigin
def SaveEditSubCategoryIcon(request):
    try:
        categoryid=request.POST['categoryid']
        result=request.session['EMPLOYEE']
        try:
            subcategoryid=request.POST['subcategoryid']
            oldpicture=request.POST['oldicon']
            picture=request.FILES['subcategoryicon']
            filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
            q="update subcategories set subcategoryicon='{}' where subcategoryid={}".format(filename,subcategoryid)
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
            return HttpResponseRedirect('/displaysubcategoriesemployee/?categoryid={}'.format(categoryid))
            
        except Exception as e:
            print("Error:", e)
            return HttpResponseRedirect('/displaysubcategoriesemployee/?categoryid={}'.format(categoryid)) 
    except Exception as e:
        print('error@195:',e)
        return EmployeeLogin(request)          

@xframe_options_sameorigin                          
def DisplayAllSubCategoriesEmployee(request):
    try:
        result=request.session['EMPLOYEE']
        print('request:',request)
        db,cmd=Pool.ConnectionPool()
        q="select * from subcategories "
        cmd.execute(q)
        rows=cmd.fetchall()
        return render(request,'DisplaySubCategoriesEmployee.html',{'rows':rows})
    except Exception as e:
        print('error',e)
        return EmployeeLogin(request)                         