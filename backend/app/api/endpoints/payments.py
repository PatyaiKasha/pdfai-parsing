from fastapi import APIRouter, Depends, Request, Response, status
from typing import Any
import json

from app.api import deps
from app.models.user import User as UserModel

router = APIRouter()

@router.post("/create-checkout-session", response_model=dict, status_code=status.HTTP_200_OK)
def create_checkout_session(
    current_user: UserModel = Depends(deps.get_current_active_user),
) -> Any:
    """
    Create a mock checkout session for a payment provider.

    This endpoint simulates the creation of a checkout session for upgrading
    a user's plan. In a real application, it would interact with a payment
    provider like Stripe.
    """
    mock_checkout_url = f"https://checkout.stripe.com/mock-session-for-user-{current_user.id}"

    return {"checkout_url": mock_checkout_url}


@router.post("/webhook", response_model=dict, status_code=status.HTTP_200_OK)
async def stripe_webhook(request: Request) -> Any:
    """
    Handle incoming webhooks from a payment provider.

    This endpoint is a stub for handling events sent by a payment provider
    (e.g., Stripe) to notify the application about subscription updates,
    payments, etc. It must be public.
    """
    try:
        payload = await request.json()
        event_type = payload.get("type", "unknown_event")

        print(f"--- Received Webhook Event ---")
        print(f"Event Type: {event_type}")
        print(f"Payload: {json.dumps(payload, indent=2)}")
        print(f"------------------------------------")

        return {"status": "received"}

    except json.JSONDecodeError:
        return Response(content="Invalid JSON payload", status_code=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response(content=f"Webhook processing error: {e}", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
