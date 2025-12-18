from django.shortcuts import render
from django.http import HttpResponse
from EMS.models import Employee,Customer

# Create your views here.

# Q1.Wap to check number is equal to 100 or not.
# def viewHome(request):
#     d1 = {'a': 55}
#     resp = render(request, "EMS/home.html", context=d1)
#     return resp



# Q2.Write a program to check smallest of two numbers.
# def viewHome(request):
#     d1 = {'x':200,'y':150}
#     resp = render(request,"EMS/home.html",context=d1)
#     return resp


# def viewCalc(request):
#     a = int(request.POST.get('t1',0))
#     b = int(request.POST.get("t2",0))
#     if request.method == "GET":
#         resp = render(request,'EMS/calc.html')
#         return resp
#     elif request.method == "POST":
#         if 'btnSum' in request.POST:
#             c = a+b
#             print(c)

#     d1 = {'c':c,'a':a,'b':b}
#     resp = render(request,'EMS/calc.html',context=d1)
#     return resp



# def viewHome2(request):
#     b= 19
#     result = [(i, b * i) for i in range(1, 11)]   # (input number, multiplication result)
#     print("--------------------",result)

#     d1 = {"b": b,"table": result}

#     return render(request, "EMS/home2.html", context=d1)



# class Employee:
#     def __init__(self):
#         self.name = ""
#         self.age = 0
#         self.address = ""
#         self.mobileno = ""
#         self.post = ""
#         self.salary = 0

# def get_N_Employee(n):
#     empList = []
#     for i in range(1,n+1):
#         emp = Employee()
#         emp.name = "Prajakta"+str(i)
#         emp.age = 28+i
#         emp.address = "Texas"+ str(i)
#         emp.mobileno = "123456789"+ str(i)
#         emp.post = "fullstack"+ str(i)
#         emp.salary= 78000+i
#         empList.append(emp)
#     return empList

# def view_home(request):
#     empNo = int(request.POST.get('txtNo',0))
#     # print("-------------------empNO----------------",empNo)
#     employee = get_N_Employee(empNo)
#     # for emp in employee:
#     #     print(emp.name)
#         # print(emp.age)
#         # print(emp.address)
#         # print(emp.mobileno)
#         # print(emp.post)
#         # print(emp.salary)
#     d1 = {'employee':employee}
#     # resp = HttpResponse("<h1>Hello I am calling DTL using For Loop</h1>")
#     # return resp
#     resp = render(request,"EMS/home2.html",context=d1)
#     return resp


def view_insert_ems(request):
    if request.method == "GET":
        resp = render(request,"EMS/insertems.html")
        return resp
    elif request.method == "POST":
        emp = Employee()
        emp.name = request.POST.get("txtName","NA")
        emp.age = int(request.POST.get("txtAge",0))
        emp.mobileno = request.POST.get("txtMobileno","NA")
        emp.address = request.POST.get("txtAddress","NA")
        emp.save()
        resp = HttpResponse("<h1>Employee Inserted Successfully!! Done</h1>")
        return resp
    


def viewCustomer(request):
    cus = Customer()
    if request.method == "GET":
        resp = render(request,'EMS/customer.html')
        return resp
    elif 'btnAdd' in request.POST:
        
        cus.name = request.POST.get("txtName","NA")
        # print("----------------------",name)
        cus.age = int(request.POST.get("txtAge",0))
        cus.address = request.POST.get('txtAdd',"NA")
        cus.mobileNo = request.POST.get('txtMob',"NA")
        cus.salary = float(request.POST.get('txtSal',0))
        cus.save()
        resp = render(request,"EMS/customerDataAddedSuccess.html")
        return resp
    elif 'btnSearch' in request.POST:
        cus_id = int(request.POST.get('txtID',0))
        # print("-------------------",cus_id)
        customer_id=Customer.objects.get(id=cus_id)
        # print("---------------CUS ID--------------",customer_id)
        d1 = {'customer':customer_id}
        resp = render(request,"EMS/customer.html",context=d1)
        return resp
    elif 'btnUpdate' in request.POST:
        cus1 = Customer()
        cus1.id = int(request.POST.get("txtID",0)) # 1
        if Customer.objects.filter(id=cus1.id).exists():
            cus1.name = request.POST.get('txtName',"NA")
            cus1.age = int(request.POST.get("txtAge",0))
            cus1.address = request.POST.get('txtAdd','NA')
            cus1.mobileNo = request.POST.get("txtMob","NA")
            cus1.salary = float(request.POST.get("txtSal",0))
            cus1.save()
            resp = HttpResponse("<h1>Customer Data Updated Successfully!!</h1>")
            return resp
    elif 'btnDelete' in request.POST:
        cus2 = Customer()
        cus2.id = int(request.POST.get("txtID",0)) # 1
        if Customer.objects.filter(id=cus2.id).exists():
            # Customer.objects.delete(id)
            Customer.objects.get(id=cus2.id).delete()
            resp = HttpResponse("<h1>Customer Deleted Succussfully!!<h1>")
            return resp














    


