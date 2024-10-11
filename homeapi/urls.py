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
    path("spreadsheet/<str:sheet_id>/", ListData.as_view(), name="mainSheetData"),
    path(
        "spreadsheet/<str:sheet_id>/given/",
        ListDataGiven.as_view(),
        name="givenSheetData",
    ),
    path(
        "spreadsheet/<str:sheet_id>/add/<str:user>/<str:sheet>/",
        CreateRow.as_view(),
        name="create_row",
    ),
    path(
        "spreadsheet/<str:sheet_id>/add/<str:user>/<int:day>/<str:sheet>/",
        CreateRow.as_view(),
        name="create_row_with_day",
    ),
    path(
        "spreadsheet/<str:sheet_id>/update/<int:day>/<str:user>/<str:sheet>/",
        UpdateRow.as_view(),
        name="update_row",
    ),
    path(
        "spreadsheet/<str:sheet_id>/delete/<int:day>/<str:sheet>/",
        DeleteRow.as_view(),
        name="delete_row",
    ),
    path(
        "spreadsheet/<str:sheet_id>/total/<str:user>/",
        GetTotal.as_view(),
        name="totalEachUser",
    ),
    path("spreadsheet/<str:sheet_id>/total/", GetTotal.as_view(), name="total"),
    path("spreadsheet/<str:sheet_id>/users/", GetAllUsers.as_view(), name="all_users"),
    path(
        "spreadsheet/<str:sheet_id>/get/<str:user>/<str:sheet>/",
        GetUserMeal.as_view(),
        name="get_user_meal",
    ),
]
