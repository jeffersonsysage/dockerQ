from typing import List, Optional
from pydantic import BaseModel, Field
from datetime import datetime, timedelta

class JUser(BaseModel):
    name: str
    email: str