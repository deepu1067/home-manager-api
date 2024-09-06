from django.urls import path
from .views import ListData

urlpatterns = [
    # path('create/', CreateRow.as_view(), name='create_row'),
    path('', ListData.as_view(), name='list_data')
    # path('update/<str:range_>/', UpdateRow.as_view(), name='update_row'),
    # path('delete/<str:range_>/', DeleteRow.as_view(), name='delete_row'),
]
