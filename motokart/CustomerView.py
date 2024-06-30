from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from numpy import short
from motokart.CategoryView import *
from . import PoolDict
from . import Pool
from django.http import JsonResponse
from django.views.decorators.clickjacking import xframe_options_sameorigin
import uuid
import os

@xframe_options_sameorigin
def CustomerHomepage(request):
    try:
        result=request.session['CUSTOMER']
        try:
            db,cmd=Pool.ConnectionPool()
            q="select * from categories"
            cmd.execute(q)
            rows=cmd.fetchall()
            return render(request,'CustomerDashboard.html',{'rows':rows})
        except Exception as e:
            print('errorrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrr:',e)
            return render(request,'CustomerDashBoard.html',{'rows':[]})
    except Exception as e:
        print('error@27:',e)
        db,cmd=Pool.ConnectionPool()
        q="select * from categories"
        cmd.execute(q)
        rows=cmd.fetchall()
        return render(request,'CustomerHomepage.html',{'rows':rows})


@xframe_options_sameorigin
def CustomerLoginRegister(request):
    try:
        result=request.session['CUSTOMER']
        db,cmd=Pool.ConnectionPool()
        q="select * from categories"
        cmd.execute(q)
        rows=cmd.fetchall()
        return render(request,'CustomerDashboard.html',{'rows':rows})
    except Exception as e:
        print('errorr',e)    
        return render(request,'CustomerLoginRegister.html',{'msgl':'Please login first!','msgr':'Or you can Register!'})       

@xframe_options_sameorigin
def CustomerRegistration(request):
    try:
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        if(password==confirmpassword):
            return render(request,'CustomerRegistration.html',{'username':username,'password':password,'msg':''})
        else:
            return render(request,'CustomerLoginRegister.html',{'msgl':'Please login first!','msgr':'Password does not match!'})        
    except Exception as e:
        print('errrorrrrrrrrr',e)
        return render(request,'CustomerLoginRegister.html',{'msgl':'Please login first!','msgr':'Or you can Register!'})

@xframe_options_sameorigin
def SubmitCustomer(request):
    try:
        username=request.POST['username']
        password=request.POST['password']
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        customeremail=request.POST['customeremail']
        customerphone=request.POST['customerphone']
        gender=request.POST['gender']
        address=request.POST['address']
        stateid=request.POST['stateid']
        cityid=request.POST['cityid']
        pincode=request.POST['pincode']
        q="insert into customers(firstname,lastname,username,customeremail,customerphone,gender,stateid,cityid,address,pincode,password)values('{}','{}','{}','{}','{}','{}',{},{},'{}','{}','{}')".format(firstname,lastname,username,customeremail,customerphone,gender,stateid,cityid,address,pincode,password)
        db,cmd=Pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        q="select * from categories"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,'CustomerLoginRegister.html',{'rows':rows,'msgl':'Record submission done! check your login here','msgr':''})

    except Exception as e:
        print('errrrrrrrrrorrrrr',e)
        return render(request,'CustomerRegistration.html',{'password':password,'username':username,'msg':'!Record Submission Unsucesfull'})

@xframe_options_sameorigin        
def GetUsernameJSON(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select username from customers"
        cmd.execute(q)
        rows=cmd.fetchall()
        return JsonResponse(rows,safe=False)
    except Exception as e:
        print('error',e)
        return JsonResponse(rows,safe=False)    
# xframe_options_sameorigin
# def CustomerLogin(request):
#     try:
#         result=request.session['CUSTOMER']
#         db,cmd=Pool.ConnectionPool()
#         q="select * from categories"
#         cmd.execute(q)
#         rows=cmd.fetchall()
#         db.close()
#         return render(request, "CustomerHomepage.html", {'rows':rows})
#     except Exception as e:
#         q="select * from categories"
#         cmd.execute(q)
#         rows=cmd.fetchall()
#         db.close()
#         return render(request,'CustomerLoginRegister.html',{'rows':rows,'msgr':''})                

@xframe_options_sameorigin
def CheckCustomerLogin(request):
    try:
        try:
            result=request.session['CUSTOMER']
            db,cmd=Pool.ConnectionPool()
            q="select * from categories"
            cmd.execute(q)
            rows=cmd.fetchall()
            return render(request,'CustomerDashboard.html',{'rows':rows})
        except Exception as e:    
            username=request.POST['username']
            password=request.POST['password']
            db,cmd=PoolDict.ConnectionPool()
            q="select * from customers where username='{}' and password='{}' ".format(username,password)
            cmd.execute(q)
            result=cmd.fetchone()
            db,cmd=Pool.ConnectionPool()
            q="select * from categories"
            cmd.execute(q)
            rows=cmd.fetchall()
            db.close()
            if(result):
                request.session['CUSTOMER']=result
                return render(request,"CustomerDashboard.html",{'rows':rows})
            else:
                db,cmd=Pool.ConnectionPool()
                q="select * from categories"
                cmd.execute(q)
                rows=cmd.fetchall()
                db.close()
                return CustomerHomepage(request)  
    
    except Exception as e:
        print(e)
        db,cmd=Pool.ConnectionPool()
        q="select * from categories"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,"CustomerLoginRegister.html",{'rows':rows,'msgr':'','msgl':'Server error'})

@xframe_options_sameorigin
def CustomerLogout(request):
    try:
        del request.session['CUSTOMER']
        db,cmd=Pool.ConnectionPool()
        q="select * from categories"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,'CustomerHomepage.html',{'rows':rows})  
    except Exception as e:
        print('error@175:',e)
        db,cmd=Pool.ConnectionPool()
        q="select * from categories"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,'CustomerHomepage.html',{'rows':rows})    
    
@xframe_options_sameorigin
def CustomerSearch(request):
    try:
        pattern=request.GET['pattern']
        # print("printttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt",request)
        # print('pattern:',pattern)
        db,cmd=Pool.ConnectionPool()
        q="select * from products where productname like '%{}%' or shortdescription like '%{}%' or moredescription like '%{}%'".format(pattern,pattern,pattern)
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,'CustomerSearch.html',{'rows':rows})
    except Exception as e:
        print('errror@187:',e) 
        return render(request,'CustomerSearch.html',{'rows':[]})

@xframe_options_sameorigin
def CustomerLoginOptions(request):
    try:
        result=request.session['CUSTOMER']
        return render(request,'CustomerLoginOptions.html') 
    except Exception as e:
        print('error@206:',e)
        return render(request,'CustomerLoginRegister.html',{'msgl':'Please login first!','msgr':'Or you can Register!'}) 
                  

@xframe_options_sameorigin
def CustomerEditProfile(request):
    try:
        result=request.session['CUSTOMER']
        db,cmd=Pool.ConnectionPool()
        q="select statename from states where stateid={}".format(result.get('stateid'))  
        cmd.execute(q)
        statename=cmd.fetchone() 
        q="select cityname from cities where cityid={}".format(result.get('cityid'))  
        cmd.execute(q)
        cityname=cmd.fetchone() 
        return render(request,'CustomerEditProfile.html',{'result':result,'statename':statename[0],'cityname':cityname[0]})
    except Exception as e:
        print('error@214',e)
        return render(request,'CustomerLoginRegister.html',{'msgl':'Please login first!','msgr':'Or you can Register!'})    

@xframe_options_sameorigin
def CustomerUpdate(request):
    try:
        result=request.session['CUSTOMER']
        customerid=request.GET['customerid']
        firstname=request.GET['firstname']
        lastname=request.GET['lastname']
        customeremail=request.GET['customeremail']
        customerphone=request.GET['customerphone']
        gender=request.GET['gender']
        address=request.GET['address']
        stateid=request.GET['stateid']
        cityid=request.GET['cityid']
        pincode=request.GET['pincode'] 
        db,cmd=Pool.ConnectionPool()
        q="update customers set firstname='{}',lastname='{}' ,customeremail='{}',customerphone='{}',gender='{}',address='{}',stateid={},cityid={},pincode='{}' where customerid={}".format(firstname,lastname,customeremail,customerphone,gender,address,stateid,cityid,pincode,customerid)
        print('hiiiiiiiiiiiiiiiiiiiiiiiiii:',q)
        cmd.execute(q)
        db.commit()
        db.close()
        db,cmd=PoolDict.ConnectionPool()
        q="select * from customers where customerid={}".format(customerid)
        cmd.execute(q)
        result=cmd.fetchone()
        request.session['CUSTOMER']=result
        db.close()
        db,cmd=Pool.ConnectionPool()
        q="select statename from states where stateid={}".format(result.get('stateid'))  
        cmd.execute(q)
        statename=cmd.fetchone() 
        q="select cityname from cities where cityid={}".format(result.get('cityid'))  
        cmd.execute(q)
        cityname=cmd.fetchone() 
        return render(request,'CustomerProfile.html',{'result':result,'statename':statename[0],'cityname':cityname[0],'msg':'Profile Update Sucessful!'})
    except Exception as e:
        print('error@244:',e)
        result=request.session['CUSTOMER']
        db,cmd=Pool.ConnectionPool()
        q="select statename from states where stateid={}".format(result.get('stateid'))  
        cmd.execute(q)
        statename=cmd.fetchone() 
        q="select cityname from cities where cityid={}".format(result.get('cityid'))  
        cmd.execute(q)
        cityname=cmd.fetchone() 
        return render(request,'CustomerProfile.html',{'result':result,'statename':statename[0],'cityname':cityname[0],'msg':'Profile Update Unsucessful!'})

@xframe_options_sameorigin
def CustomerProfile(request):
    try:
        result=request.session['CUSTOMER']
        db,cmd=Pool.ConnectionPool()
        q="select statename from states where stateid={}".format(result.get('stateid'))  
        cmd.execute(q)
        statename=cmd.fetchone() 
        q="select cityname from cities where cityid={}".format(result.get('cityid'))  
        cmd.execute(q)
        cityname=cmd.fetchone() 
        return render(request,'CustomerProfile.html',{'result':result,'statename':statename[0],'cityname':cityname[0],'msg':''})
    except Exception as e:
        print('error@258',e)
        return render(request,'CustomerLoginRegister.html',{'msgl':'Please login first!','msgr':'Or you can Register!'})    

@xframe_options_sameorigin
def CustomerUpdateUsernamePassword(request):
    try:
        result=request.session['CUSTOMER']
        return render(request,'CustomerUpdateUsernamePassword.html',{'result':result})
    except Exception as e:
        return render(request,'CustomerLoginRgister.html',{'msgl':'Please login first!','msgr':'Or you can Register!'})

@xframe_options_sameorigin
def CustomerUpdateUsername(request):
    try:
        result=request.session['CUSTOMER']
        try:
            username=request.POST['username']
            db,cmd=Pool.ConnectionPool()
            q="update customers set username='{}' where customerid={}".format(username,result.get('customerid'))
            cmd.execute(q)
            db.commit()
            result['username']=username
            request.session['CUSTOMER']=result
            return render(request,'CustomerUpdateUsernamePassword.html',{'result':result,'msgl':'Username Updated Sucessfully!','msgr':''})
        except Exception as e:
            print('error@302:',e)
            return render(request,'CustomerUpdateUsernamePassword.html',{'msgl':'Username Update Unsucessful!','msgr':''})
    except Exception as e:
        return CustomerLoginRegister(request)

@xframe_options_sameorigin
def CustomerUpdatePassword(request):
    try:
        result=request.session['CUSTOMER']
        try:
            oldpassword=request.POST['oldpassword']
            newpassword=request.POST['newpassword']
            confirmpassword=request.POST['confirmpassword']
            if(oldpassword==result.get('password')):
                if(newpassword==confirmpassword):
                    db,cmd=Pool.ConnectionPool()
                    q="update customers set password='{}' where customerid={}".format(newpassword,result.get('customerid'))
                    cmd.execute(q)
                    db.commit()
                    result['password']=newpassword
                    request.session['CUSTOMER']=result
                    return render(request,'CustomerUpdateUsernamePassword.html',{'result':result,'msgl':'','msgr':'Password Updated Sucessfully!'})
                else:
                    return render(request,'CustomerUpdateUsernamePassword.html',{'result':result,'msgl':'','msgr':'Password Does not match'})
            else:
                return render(request,'CustomerUpdateUsernamePassword.html',{'result':result,'msgl':'','msgr':'Previous Password does not match!'})

        except Exception as e:
            print('error@302:',e)
            return render(request,'CustomerUpdateUsernamePassword.html',{'msgl':'','msgr':'Password Update Unsucessful!'})
    except Exception as e:
        return CustomerLoginRegister(request)        


@xframe_options_sameorigin
def PaymentPage(request):
    try:
        result=request.session['CUSTOMER']
        db,cmd=Pool.ConnectionPool()
        q="select statename from states where stateid={}".format(result.get('stateid'))  
        cmd.execute(q)
        statename=cmd.fetchone() 
        q="select cityname from cities where cityid={}".format(result.get('cityid'))  
        cmd.execute(q)
        cityname=cmd.fetchone() 
        return render(request,'PaymentPage.html',{'result':result,'statename':statename[0],'cityname':cityname[0]})
    except Exception as e:
        return render(request,'CustomerLoginRegister.html',{'msgl':'Please login first!','msgr':'Or you can Register!'})  

@xframe_options_sameorigin
def AddToWishlist(request):
    try:
        result=request.session['CUSTOMER']
        productid=request.GET['productid']
        customerid=result.get('customerid')
        db,cmd=Pool.ConnectionPool()
        try:
            q="insert into wishlist (customerid,productid) values({},{})".format(customerid,productid)
            cmd.execute(q)
            db.commit()
            db.close()
            return ShowWishlist(request)
        except Exception as e:
            print('error@300:',e)
            try:
                return ShowWishlist(request)
            except Exception as e:  
                print('error@307',e)  
    except Exception as e:
        print('error@306:',e)
        return render(request,'CustomerLoginRegister.html',{'msgl':'Please login first!','msgr':'Or you can Register!'})   

@xframe_options_sameorigin
def ShowWishlist(reqest):
    try:
        result= reqest.session['CUSTOMER']
        db,cmd=Pool.ConnectionPool()
        q="select productid from wishlist where customerid={}".format(result.get('customerid'))
        cmd.execute(q)
        productsid=cmd.fetchall()
        rows=()
        for productid in productsid:
            q="select * from products where productid={}".format(productid[0])
            cmd.execute(q)
            row=cmd.fetchone()
            rows+=(row,)
        return render(reqest,'ShowWishlist.html',{'rows':rows}) 
    except Exception as e:
        print('error@330',e)
        return render(reqest,'CustomerLoginRegister.html',{'msgl':'Please login first!','msgr':'Or you can Register!'})

@xframe_options_sameorigin
def RemoveFromWishlist(request):
    try:
        result= request.session['CUSTOMER']
        productid=request.GET['productid']
        db,cmd=Pool.ConnectionPool()
        q="delete from wishlist where customerid={} and productid={}".format(result.get('customerid'),productid)
        cmd.execute(q)
        db.commit()
        db.close()
        return ShowWishlist(request)
    except Exception as e:
        print('error@348',e)
        return render(request,'CustomerLoginRegister.html',{'msgl':'Please login first!','msgr':'Or you can Register!'})


         



