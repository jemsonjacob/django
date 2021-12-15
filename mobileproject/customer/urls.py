from django.urls import path
from customer import views

# customer/accounts/signup=>registration
# customer/accounts/signin=>login
# customer/accounts/signout=>logout


urlpatterns = [
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/signin', views.signin, name='signin'),
    path('accounts/signout', views.signout, name='signout'),
    path("",views.user_home,name="user_home"),
    path('orders/add/<int:p_id>',views.order_create,name="ordercreate"),
    path('mobiles/orders',views.order_list,name="list_orders"),
    path('mobiles/orders/remove/<int:p_id>',views.cancel_order,name="cancel_order"),
    path('mobiles/find',views.mobile_find,name="mobile_find")
]
