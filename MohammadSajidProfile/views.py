from django.views import View
from django.shortcuts import render

class IndexView(View):
    template_name = "index.html"
    def get(self,request):
        return render(request,self.template_name)

class AboutView(View):
    template_name = "about.html"
    def get(self,request):
        return render(request,self.template_name)
class ContactView(View):
    template_name = "contact.html"
    def get(self,request):
        return render(request,self.template_name)