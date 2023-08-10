
from django.shortcuts import render,redirect
from  django.http import HttpResponse, HttpResponseNotFound, Http404
from django.urls import reverse
from datetime import date,datetime
from .models import Course,Person,Category

data={
   "mobil":"moblimsi",
   "tel":"telefonumsu",
   "pc":"pc msi",
   
}

db={
   "courses":[
      {

         "title":"javascript kursu",
         "description":"javascript kurs açıklması",
         "imageUrl":"2.jpg",
         "slug":"javascript-kursu",
         "date":datetime.now(),
         "isActive":True,
         "isUpdated":True
      },
       {

         "title":"python kursu",
         "description":"python kurs açıklması",
         "imageUrl":"3.png",
         "slug":"python-kursu",
         "date":date(2022,10,10),
          "isActive":True,
          "isActivated":True
      },
       {

         "title":"web geliştirme kursu",
         "description":"web-geliştirme kurs açıklması",
         "imageUrl":"1,jpg",
         "slug":"web-gelistirme-kursu",
         "isActive":True
      }
   ],
   "categories":[
      {"id":1, "name":"programlama", "slug":"programlama"},
                { "id":2, "name":"web geliştirme", "slug":"web-geliştirme"},
               { "id":3, "name":"mobil uygulamalar", "slug":"mobil-uygulamalar"}]
}



#def kurslar(request):
  # list_items=""
     # for category in category_list:
    #   redirect_url= reverse('courses_by_category',args=[category])
    #  list_items += f"<li><a href='{redirect_url}'>{category}</a></li>"
 #sayfa=f"<h1> kurs listesi<h/><br><ul>{list_items}</ul>"
   # return HttpResponse(sayfa+"Görünlerler listedir")


      #   category_list=list(data.keys())

     #    return render(request,'../courses/templates/indexi.html',{
       #      'categories':category_list
      #   })

def details(request,kurs_id):
      course=Course.objects.get(pk=kurs_id)
      context={
         'course':course
      }

      return render(request,'course/details.html',context)


def getCourses(request,category_name):

   try:
      category_text= data[category_name]
     
      return render(request, 'courses/kurslar.html',{#html.parametresinden sonra çıktı olarak gönderir.
                           'category': category_name,
                           'category_text': category_text})
   
   except:
    return HttpResponseNotFound('<h1>yanlis kategori</h1>')


def getCoursesId(request, category_id):
   category_list=list(data.keys())
   if (category_id > len(category_list)):
      return  HttpResponseNotFound("yanlis kategori secimi")
      return render(request, 'courses/courses.html')
   
   category_name  =category_list[category_id-1]

   redirect_url= reverse('courses_by_category',args=[category_name])
   
   return redirect(redirect_url)

def index(request):
   #  category_list=list(data.keys())

   #  return render(request, 'courses/index.html',{
   #     'categories': categoryqu_list
   #  })

   kurslar=Course.objects.all()
   kategoriler=Category.objects.all()

   return render(request, 'courses/index.html',{
      'categories': kategoriler,
      'courses': kurslar
   })

def newindex(request):
    return render(request, "courses/newindex.html")

def test(request):
   return render(request, "courses/test.html")

def kurslar(request):
    categories = Category.objects.all()
    category = "Kategori Adı"  # Bu kısmı gerçek verilere göre doldurmalısınız
    category_text = "Kategori açıklaması"  # Bu kısmı gerçek verilere göre doldurmalısınız

    context = {
        'categories': categories,
        'category': category,
        'category_text': category_text,
    }

    return render(request, 'courses/kurslar.html', context)




    
    
