from django.shortcuts import render
from django.views import View # <- View class to handle requests
from django.http import HttpResponse # <- a class to handle sending a type of response
from django.views.generic.base import TemplateView
# Create your views here.
class Index:
    def __init__(self, name, image, bio):
        self.name = name
        self.image = image
        self.bio = bio

Indexes = [
  Index("Vitelotte", "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a9/Vitelotte.jpg/1200px-Vitelotte.jpg",
          "a gourmet French variety of blue-violet potato. It has been cultivated in France at least since the early nineteenth century."),
  Index("Bintje",
          "https://harvesting-history.com/wp-content/uploads/2017/01/HH_Potato_Bintje.jpg", "Bintje is a middle-early ripening potato variety bred in the Netherlands by the Frisian schoolmaster K.L. de Vries in 1904 from and marketed for the first time in 1910. "),
  Index("Kerr's Pink", "http://specialtyproduce.com/sppics/16382.png",
          "a potato cultivar in wide production in Ireland and the United Kingdom and many other countries. Although often quoted as an 'Irish potato', the cultivar was actually created by J. Henry of Cornhill, Scotland, in 1907."),                       
]
class Home(TemplateView):
    template_name = "home.html"

class About(TemplateView):
    template_name = "about.html"

class Index(TemplateView):
    template_name = "index.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Indexes"] = Indexes # this is where we add the key into our context object for the view to use
        return context