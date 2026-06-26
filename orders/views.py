"""Views for the orders app."""

from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Order, RefundRequest


@login_required
def orders_list(request):
    """Display a list of orders for the logged-in user."""
    orders = Order.objects.filter(user=request.user)
    context = {"orders": orders}
    return render(request, "orders_list.html", context)


@login_required  # ← missing, anyone could access /orders/1/ without logging in
def order_detail(request, order_id):
    """Display the details of a single order."""
    order = get_object_or_404(
        Order, pk=order_id, user=request.user
    )  # ← removed duplicate Order

    # get refund history
    refunds = RefundRequest.objects.filter(order=order)

    context = {
        "order": order,
        "refunds": refunds,
    }
    return render(request, "order_detail.html", context)
