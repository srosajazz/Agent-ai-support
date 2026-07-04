from orders.models import Order
from django.utils import timezone


def get_order_details(order_id):
    """Tool: looks up an order and returns its status, carrier, tracking number, and date."""
    try:
        order = Order.objects.get(id=order_id)  # fetch the order by its primary key
    except Order.DoesNotExist:
        return {
            "error": f"Order #{order_id} not found."
        }  # tool result the agent can relay to the customer

    return {
        "order_id": order.id,
        "product_name": order.product_name,
        "amount": str(order.amount),  # type: ignore
        "status": order.status,  # e.g. "shipped", "delivered", "processing"
        "carrier": order.carrier,  # e.g. "BlueDart"
        "tracking_number": order.tracking_number,
        "order_date": order.created_at.isoformat(),# ISO format so it's JSON-serializable
         "days_since_order": (timezone.now() = order.crated_at).days, # 20 days
        # "ordered_on": order.created_at.strftime("%d %b %Y"),
    }
