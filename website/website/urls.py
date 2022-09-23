from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from blog import views as blog_views
from shop import views as shop_views
from account import views as account_views

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

    path('product/', shop_views.product_list, name='product-list'),
    path('product/<int:id>', shop_views.product_detail, name='product-detail'),
    path('product/<int:id>/add-to-cart', shop_views.add_to_cart, name='add-to-cart'),
    path('signup/', account_views.signup, name='signup'),
    path('login/', account_views.login_user, name='login'),
    path('logout/', account_views.logout_user, name='logout'),

    path('contact-us/', blog_views.contact, name='contact'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
