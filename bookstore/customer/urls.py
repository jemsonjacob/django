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
    path('books/orders',views.orders_list,name="list_orders"),
    path('books/orders/remove/<int:id>',views.cancel_order,name="cancell_order"),
    path('books/find',views.book_find,name="findbook")
]
