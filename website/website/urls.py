from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog import views as blog_views
from shop import views as shop_views


from website import settings

urlpatterns = [
    path('', shop_views.index, name='index'),
    path('admin/', admin.site.urls),
    path('personnages/', blog_views.character_list, name='character-list'),
    path('personnages/<int:id>/', blog_views.character_detail, name='character-detail'),
    path('saga/', blog_views.saga_list, name='saga-list'),
    path('saga/<int:id>/', blog_views.saga_detail, name= 'saga-detail'),
    path('place/', blog_views.place_list, name='place-list'),
    path('place/<int:id>/', blog_views.place_detail, name= 'place-detail'),
    path('about-us/', blog_views.about, name='about'),
    path('contact-us/', blog_views.contact, name='contact'),
    path('shop/', shop_views.product_list, name='product-list'),
    path('shop/<int:id>', shop_views.product_detail, name='product-detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
