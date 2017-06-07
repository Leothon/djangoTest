# _*_ coding: utf-8 _*_
from django.http import HttpResponse
from TestModel.models import Test

#database action
def testdb(request):
    #init
    response=""
    response1=""

    #Select * from
    list=Test.objects.all()

    #WHERE
    response2=Test.objects.filter(id=1)

    #get single object
    #response3=Test.objects.get(id=3)

    #OFFSET 0 LIMIT 2
    Test.objects.order_by('name')[0:2]

    #data sort
    Test.objects.order_by("id")

    Test.objects.filter(name="Leothon").order_by("id")

    #print all data

    for var in list:
        response1+=var.name+""
    response=response1
    return HttpResponse("<p>"+response+"</p>")