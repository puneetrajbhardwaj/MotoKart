from django.shortcuts import render
from . import PoolDict
from . import Pool
from django.views.decorators.clickjacking import xframe_options_sameorigin

def EmployeeLogin(request):
    try:
        result=request.session['EMPLOYEE']
        return render(request, "EmployeeDashboard.html", {'result': result})
    except Exception as e:
        return render(request,'EmployeeLogin.html',{'msg':''})

def CheckEmployeeLogin(request):
    try:
        try:
            result=request.session['EMPLOYEE']
            return render(request,'EmployeeDashboard.html')
        except Exception as e:    
            employeeemail=request.POST['employeeemail']
            password=request.POST['password']
            db,cmd=PoolDict.ConnectionPool()
            q="select * from employees where employeeemail='{}' and password='{}' ".format(employeeemail,password)
            cmd.execute(q)
            result=cmd.fetchone()
            print(result)
            db.close()
            if(result):
                request.session['EMPLOYEE']=result
                return render(request,"EmployeeDashboard.html",{'result':result})
            else:
                return render(request,"EmployeeLogin.html",{'result':{},'msg':'Invalid Email or Password'})
            
    except Exception as e:
        print(e)
        return render(request,"EmployeeLogin.html",{'result':{},'msg':'Server Error'})


def EmployeeLogout(request):
    try:
        del request.session['EMPLOYEE']
        return render(request,'EmployeeLogin.html',{'msg':''})
    except Exception as e:
        print('error@43:',e)
        return render(request,'EmployeeLogin.html',{'msg':'Kindly! login'})    

@xframe_options_sameorigin
def EmployeeSearch(request):
    try:
        result=request.session['EMPLOYEE']
        try:
            pattern=request.GET['pattern']
            # print("printttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt",request)
            # print('pattern:',pattern)
            db,cmd=Pool.ConnectionPool()
            q="select * from products where productname like '%{}%' or shortdescription like '%{}%' or moredescription like '%{}%'".format(pattern,pattern,pattern)
            cmd.execute(q)
            rows=cmd.fetchall()
            print(rows)
            db.close()
            return render(request,'EmployeeSearch.html',{'rows':rows})
        except Exception as e:
            print('errror@56:',e) 
            return render(request,'EmployeeSearch.html',{'rows':[]})
    except Exception as e:
        print('error@65:',e) 
        return EmployeeLogin(request)       


# def DisplayAllSubCategoriesEmployee(request):
#     try:
#         db,cmd=Pool.ConnectionPool()
#         q="select S.* ,(select C.categoryname from categories C where C.categoryid=S.categoryid) from subcategories S"
#         cmd.execute(q)
#         rows=cmd.fetchall()
#         return render(request,'DisplaySubcategories.html',{'rows':rows})
#     except Exception as e:
#         print('error',e)
#         return render(request,'DisplaySubcategories.html', {'rows':[]})