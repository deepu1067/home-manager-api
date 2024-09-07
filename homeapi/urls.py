from django.urls import path
from .views import (
    ListData,
    CreateRow,
    UpdateRow,
    DeleteRow,
    ListDataGiven,
    GetTotal,
)

urlpatterns = [
    path("", ListData.as_view(), name="mainSheetData"),
    path("given/", ListDataGiven.as_view(), name="givenSheetData"),
    path("add/<str:sheet>/", CreateRow.as_view(), name="create_row"),
    path("add/<int:day>/<str:sheet>/", CreateRow.as_view(), name="create_row_with_day"),
    path(
        "update/<int:day>/<str:user>/<str:sheet>/",
        UpdateRow.as_view(),
        name="update_row",
    ),
    path("delete/<int:day>/<str:sheet>/", DeleteRow.as_view(), name="delete_row"),
    path("total-meal/<str:user>/<str:sheet>/", GetTotal.as_view(), name="totalMeal"),
]
