from django.db import models  # Django's ORM base class for models
from django.contrib.auth.models import (
    User,
)  # built-in User model, used as the message/conversation owner
from orders.models import (
    Order,
)  # Order model from the orders app, linked to each conversation


class Conversation(
    models.Model
):  # represents a single support/chat conversation tied to an order
    user = models.ForeignKey(  # the user who owns this conversation
        User,
        on_delete=models.CASCADE,
        related_name="conversations",  # delete conversation if user is deleted; access via user.conversations
    )
    order = models.ForeignKey(  # the order this conversation is about
        Order,
        on_delete=models.CASCADE,
        related_name="conversations",  # delete conversation if order is deleted; access via order.conversations
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # timestamp set automatically when the conversation is created

    def __str__(self):  # human-readable representation, e.g. for the Django admin
        return f"Conversation #{self.id} - {self.user.username} - Order #{self.order.id}"  # shows id, username, and order id


class Message(models.Model):  # a single message within a conversation
    ROLE_CHOICES = [  # allowed values for who sent the message
        ("user", "USER"),  # message sent by the customer
        ("agent", "AGENT"),  # message sent by the support agent
    ]

    conversation = models.ForeignKey(  # the conversation this message belongs to
        Conversation,
        on_delete=models.CASCADE,
        related_name="messages",  # delete message if conversation is deleted; access via conversation.messages
    )
    role = models.CharField(
        max_length=20, choices=ROLE_CHOICES
    )  # who sent the message, restricted to ROLE_CHOICES
    content = models.TextField()  # the message body, unlimited length
    created_at = models.DateTimeField(
        auto_now_add=True
    )  # timestamp set automatically when the message is created

    def __str__(self):  # human-readable representation, e.g. for the Django admin
        return f"{self.role}: {self.content[:50]}"  # shows role and first 50 chars of content


class AgentLog(models.Model):
    EVENT_CHOICES = [
        ("support", "Support Agent"),
        ("tool_call", "Tool Call"),
        ("tool_results", "Tool Results"),
        ("manager", "Manager Agent"),
        ("risk", "Risk Agent"),
        ("final", "Final Reply"),
    ]
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name="agentlogs"
    )
    event_type = models.CharField(max_length=20, choices=EVENT_CHOICES)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"[{self.event_type}] - {self.message[:40]}"


