from django.urls import path
from .views import (
    ListData,
    CreateRowMeal,
    UpdateRowMeal,
    DeleteRow,
    CreateRowGiven,
    UpdateRowGiven,
)

urlpatterns = [
    path("", ListData.as_view(), name="list_data"),
    path("add/", CreateRowMeal.as_view(), name="create_row"),
    path("add/<int:day>/", CreateRowMeal.as_view(), name="create_row_with_day"),
    path("update/<int:day>/<str:user>/", UpdateRowMeal.as_view(), name="update_row"),
    path("delete/<int:day>/<str:sheet>/", DeleteRow.as_view(), name="delete_row"),
    path("add_given/", CreateRowGiven.as_view(), name="create_row_given"),
    path(
        "add_given/<int:day>/",
        CreateRowGiven.as_view(),
        name="create_row_given_withDay",
    ),
    path(
        "update_given/<int:day>/<str:user>/",
        UpdateRowGiven.as_view(),
        name="update_given",
    ),
]
