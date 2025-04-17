from app1.models import IceCertificate

def certificates_processor(request):
    return {'cerf': IceCertificate.objects.all()}
