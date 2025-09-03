import uuid
from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    sub: uuid.UUID # 'sub' is standard for subject, which is the user id

# The technical specification also mentions:
# POST /api/v1/auth/register -> response_model=UserResponse
# POST /api/v1/auth/login -> response_model=TokenResponse
# So, the schemas from user.py will be used for registration responses,
# and the Token schema defined here will be used for login responses.
# This aligns with the plan.
