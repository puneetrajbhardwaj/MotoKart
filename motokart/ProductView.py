from select import select
from unittest import result
from django.shortcuts import render
from django.template import Engine, engines
from django.http import HttpResponseRedirect
import os

from requests import session

from motokart.EmployeeView import EmployeeLogin
from . import Pool
from django.http import JsonResponse
import uuid
from django.views.decorators.clickjacking import xframe_options_sameorigin


location="D:/study/wipro internship/project/data/Motokart/motokart/assets/images/"
@xframe_options_sameorigin
def ProductInterface(request):
    try:
        result=request.session['EMPLOYEE']
        return render(request,"ProductInterface.html")
    except Exception as e:
        print('error@19:',e)
        return EmployeeLogin(request)


@xframe_options_sameorigin
def ProductSubmit(request):
    try:
        result=request.session['EMPLOYEE']
        try:
            categoryid=request.POST['categoryid']
            subcategoryid=request.POST['subcategoryid']
            productname=request.POST['productname']
            company=request.POST['company']
            price=request.POST['price']
            offer=request.POST['offer']
            engine=request.POST['engine']
            power=request.POST['power']
            displacement=request.POST['displacement']
            speedtransmission=request.POST['speedtransmission']
            suspension=request.POST['suspension']
            weight=request.POST['weight']
            topspeed=request.POST['topspeed']
            shortdescription=request.POST['shortdescription']
            moredescription=request.POST['moredescription']
            icon=request.FILES['producticon']
            producticon=str(uuid.uuid4())+icon.name[icon.name.rfind('.'):]
            q="insert into products(categoryid,subcategoryid,productname,company,price,offer,engine,power,displacement,speedtransmission,suspension,weight,topspeed,shortdescription,moredescription,producticon)values({},{},'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(categoryid,subcategoryid,productname,company,price,offer,engine,power,displacement,speedtransmission,suspension,weight,topspeed,shortdescription,moredescription,producticon)
            db,cmd=Pool.ConnectionPool()
            cmd.execute(q)
            db.commit()
            F=open(location+producticon,"wb")
            for chunk in icon.chunks():
                F.write(chunk)
            F.close()
            db.close()
            return render(request,"ProductInterface.html",{'msg':'Record submitted Successfully'})
        except Exception as e:
            print('error',e)
            return render(request,"ProductInterface.html",{'msg':'Record submition failed'})
    except Exception as e:
        print('error@61',e)
        return EmployeeLogin(request)        

@xframe_options_sameorigin
def DisplayProducts(request):
    try:
        db,cmd=Pool.ConnectionPool()
        subcategoryid=request.GET['subcategoryid']
        q = "select P.*,(select C.categoryname from categories C where C.categoryid=P.categoryid),(select S.subcategoryname from subcategories S where S.subcategoryid=P.subcategoryid) from products P where P.subcategoryid={}".format(subcategoryid)
        cmd.execute(q)
        rows=cmd.fetchall()
        return render(request,'DisplayProducts.html',{'rows':rows})
    except Exception as e:
        print('error',e)
        return render(request,'DisplayProducts.html', {'rows':[]})

@xframe_options_sameorigin
def Bill(request):
    return render(request,'Bill.html')

@xframe_options_sameorigin    
def GetProductJSON(request):
    try:
        dbe, cmd = Pool.ConnectionPool()
        subcategoryid = request.GET['subcategoryid']
        q = "select * from products where subcategoryid= {}".format(
            subcategoryid)
        cmd.execute(q)
        rows = cmd.fetchall()
        dbe.close()
        return JsonResponse(rows, safe=False)
    except Exception as e:
        print(e)
        return JsonResponse([], safe=False)

@xframe_options_sameorigin
def PrintBill(request):
    try:
        productid=request.GET['productid']
        db,cmd=Pool.ConnectionPool()
        q="select * from products  where productid={}".format(productid)
        cmd.execute(q)
        row=cmd.fetchone()
        return render(request,'PrintBill.html',{'row':row})
    except Exception as e:
        print('error------------------------------------------------',e)    

@xframe_options_sameorigin
def DisplayProductsEmployee(request):
    try:
        result=request.session['EMPLOYEE']
        try:
            db,cmd=Pool.ConnectionPool()
            subcategoryid=request.GET['subcategoryid']
            q = "select P.*,(select C.categoryname from categories C where C.categoryid=P.categoryid),(select S.subcategoryname from subcategories S where S.subcategoryid=P.subcategoryid) from products P where P.subcategoryid={}".format(subcategoryid)
            cmd.execute(q)
            rows=cmd.fetchall()
            return render(request,'DisplayProductsEmployee.html',{'rows':rows})
        except Exception as e:
            print('error',e)
            return render(request,'DisplayProductsEmployee.html', {'rows':[]}) 
    except Exception as e:
        print('error@123',e)
        return EmployeeLogin(request)           

@xframe_options_sameorigin
def DisplayProductById(request):
    productid=request.GET['productid']
    try:
        result=request.session['EMPLOYEE']
        db, cmd = Pool.ConnectionPool()
        q = "select P.*,C.categoryname,S.subcategoryname from products P,categories C,subcategories S where productid={} and P.categoryid=C.categoryid and P.subcategoryid=S.subcategoryid".format(productid)
        cmd.execute(q)
        row = cmd.fetchone()
        return render(request,'DisplayProductById.html', {'row': row})
    except Exception as e:
        print('error', e)
        return EmployeeLogin(request)

@xframe_options_sameorigin
def EditDeleteProduct(request):
    try:
        result=request.session['EMPLOYEE']
        btn=request.GET['btn']
        productid=request.GET["productid"]
        producticon=request.GET["producticon"]
        print("xxxxxxxxxxxx",btn)
        if(btn=="Edit"):
            categoryid=request.GET['categoryid']
            subcategoryid=request.GET['subcategoryid']
            productname=request.GET['productname']
            company=request.GET['company']
            price=request.GET['price']
            offer=request.GET['offer']
            engine=request.GET['engine']
            power=request.GET['power']
            displacement=request.GET['displacement']
            speedtransmission=request.GET['speedtransmission']
            suspension=request.GET['suspension']
            weight=request.GET['weight']
            topspeed=request.GET['topspeed']
            shortdescription=request.GET['shortdescription']
            moredescription=request.GET['moredescription']
            try:
                db, cmd = Pool.ConnectionPool()
                q = "update products set categoryid={},subcategoryid={},productname='{}',company='{}',price='{}',offer='{}',engine='{}',power='{}',displacement='{}',speedtransmission='{}',suspension='{}',weight='{}',topspeed='{}',shortdescription='{}',moredescription='{}' where productid={}".format(categoryid,subcategoryid,productname,company,price,offer,engine,power,displacement,speedtransmission,suspension,weight,topspeed,shortdescription,moredescription,productid)
                print (q)
                cmd.execute(q)
                db.commit()
                db.close()
                return DisplayProductsEmployee(request)
            except Exception as e:
                print("Error:", e)
                return DisplayProductsEmployee(request)

        elif (btn=="Delete"):

            try:
                os.remove(location+producticon)
                db, cmd = Pool.ConnectionPool()
                q = "delete from products where productid={}".format(productid)
                cmd.execute(q)
                db.commit()
                db.close()
                return DisplayProducts(request)
            except Exception as e:
                print(e)
                return DisplayProducts(request)
    except Exception as e:
        print('error@191:',e)
        return EmployeeLogin(request)            

@xframe_options_sameorigin
def EditProductIcon(request):
    try:
        result=request.session['EMPLOYEE']
        categoryid=request.GET['categoryid']
        subcategoryid=request.GET['subcategoryid']
        productid=request.GET['productid']
        productname=request.GET['productname']
        producticon=request.GET['producticon']
        row=[productid,productname,producticon,categoryid,subcategoryid]
        return render(request,"EditProductIcon.html",{'row':row})
    except Exception as e:
        print('error:',e)
        return EmployeeLogin(request)    

@xframe_options_sameorigin
def SaveEditProductIcon(request):
    categoryid=request.POST['categoryid']
    subcategoryid=request.POST['subcategoryid']
    print('------------------',subcategoryid)
    try:
        result=session.requst['EMPLOYEE']
        productid=request.POST['productid']
        oldpicture=request.POST['oldicon']
        picture=request.FILES['producticon']
        print('00000000000',oldpicture,picture)
        filename=str(uuid.uuid4())+picture.name[picture.name.rfind('.'):]
        q="update products set producticon='{}' where productid={}".format(filename,productid)
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
        return HttpResponseRedirect('/displayproductsemployee/?subcategoryid={}'.format(subcategoryid))
        
    except Exception as e:
        print("Error:", e)
        return EmployeeLogin(request)         

@xframe_options_sameorigin
def DisplayAllProductsEmployee(request):
    try:
        result=request.session['EMPLOYEE']
        db,cmd=Pool.ConnectionPool()
        q = "select * from products"
        cmd.execute(q)
        rows=cmd.fetchall()
        return render(request,'DisplayAllProductsEmployee.html',{'rows':rows})
    except Exception as e:
        print('error',e)
        return EmployeeLogin(request)   

@xframe_options_sameorigin
def SelectForComparison(request):
    return render(request,'SelectForComparision.html')
    
@xframe_options_sameorigin
def ShowComparison(request):
    productid1=request.GET['productid1']
    productid2=request.GET['productid2']
    db,cmd=Pool.ConnectionPool()
    q="select * from products where productid={}".format(productid1)
    cmd.execute(q)
    row1=cmd.fetchone()
    q="select * from products where productid={}".format(productid2)
    cmd.execute(q)
    row2=cmd.fetchone()
    return render(request,'ShowComparision.html',{'row1':row1,'row2':row2})






        


