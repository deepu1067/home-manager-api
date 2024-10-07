from django.urls import path
from .views import (
    ListData,
    CreateRow,
    UpdateRow,
    DeleteRow,
    ListDataGiven,
    GetTotal,
    GetAllUsers,
    GetUserMeal,
)

urlpatterns = [
    path("", ListData.as_view(), name="mainSheetData"),
    path("given/", ListDataGiven.as_view(), name="givenSheetData"),
    path("add/<str:user>/<str:sheet>/", CreateRow.as_view(), name="create_row"),
    path(
        "add/<str:user>/<int:day>/<str:sheet>/",
        CreateRow.as_view(),
        name="create_row_with_day",
    ),
    path(
        "update/<int:day>/<str:user>/<str:sheet>/",
        UpdateRow.as_view(),
        name="update_row",
    ),
    path("delete/<int:day>/<str:sheet>/", DeleteRow.as_view(), name="delete_row"),
    path("total/<str:user>/", GetTotal.as_view(), name="totalEachUser"),
    path("total/", GetTotal.as_view(), name="total"),
    path("users/", GetAllUsers.as_view(), name="all_users"),
    path("get/<str:user>/<str:sheet>/", GetUserMeal.as_view(), name="get_user_meal"),
]
