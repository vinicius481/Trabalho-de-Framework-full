from django.shortcuts import render


class CustomErrorServer:

    @staticmethod
    def error_500(request):
        return render(request, "500_error.html", {}, status=500)
    
    @staticmethod
    def error_404(request, exception):
        return render(request, '404_error.html', {}, status=404)