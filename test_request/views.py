from django.http import HttpResponse
from django.views import View


class TestRequest(View):

    def get(self,request):
        result = request.GET
        print(result,'\n')
        return HttpResponse('ok')
