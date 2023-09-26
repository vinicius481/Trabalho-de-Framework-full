from django.shortcuts import render
from django.http import HttpResponseForbidden


class CustomErrorServer:

    @staticmethod
    def error_500(request):
        return render(request, "500_error.html", {}, status=500)
    
    @staticmethod
    def error_404(request, exception):
        return render(request, '404_error.html', {}, status=404)
    
    @staticmethod
    def error_403(request, exception):
        return render(request, '403_error.html', {}, status=403)