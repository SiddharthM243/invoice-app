from django.urls import path
from .views import *



urlpatterns = [
    path("invoices/", AllInvoiceView.as_view(), name="invoice"),
    path("invoices/new/", AllInvoiceView.as_view(), name="newInvoices"),
    # path("invoices/<int:id>/", SingleInvoiceView.as_view(), name="singleInvoice"),
    path("invoices/<int:id>/item/", AddItemView.as_view(), name="addItem"),
    path("signup/",SignupView.as_view(),name="Signup"),
    path("signin/",SigninView.as_view(),name="Signin"),
]
