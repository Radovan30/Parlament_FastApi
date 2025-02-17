import jwt
from fastapi import HTTPException, Security, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from app.utils.auth import SECRET_KEY, ALGORITHM

security = HTTPBearer()

def get_current_admin(token: HTTPAuthorizationCredentials = Security(security)):
    try:
        payload = jwt.decode(token.credentials, SECRET_KEY, algorithms=[ALGORITHM])
        return payload["sub"]  # Vrací username admina
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expiroval")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Neplatný token")
