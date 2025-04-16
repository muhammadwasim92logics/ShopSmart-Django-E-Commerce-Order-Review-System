from django.contrib import admin
from app1.models import Items, IceReviews, Stores, IceCertificate,IceCreamImage,Customers,card

# Inline for Ice Reviews
class IceCreamReview(admin.TabularInline):
    model = IceReviews
    extra = 1
# Admin for Ice Types (Person)
class IceTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'date')
    # inlines = [IceCreamReview]
# Admin for Stores
class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('ice_type',)
# Admin for Ice Certificates
class IceCertificateAdmin(admin.ModelAdmin):
    list_display = ('ice', 'certificate_no')
# Register models
admin.site.register(Items, IceTypeAdmin)
admin.site.register(IceReviews)
admin.site.register(Stores, StoreAdmin)
admin.site.register(IceCertificate, IceCertificateAdmin)
admin.site.register(IceCreamImage)
admin.site.register(Customers)
admin.site.register(card)
