"""
User Model & Role Definitions
Defines supported roles and validation helpers for the Hunar Circle platform.
"""
from typing import Literal

ALLOWED_ROLES = {"student", "teacher"}
UserRole = Literal["student", "teacher"]
DEFAULT_ROLE: UserRole = "student"

def validate_role(role_input: str | None) -> UserRole:
    """
    Validates and normalizes role input.
    Defaults to 'student' if missing or invalid.
    """
    if not role_input or not isinstance(role_input, str):
        return DEFAULT_ROLE
    normalized = role_input.strip().lower()
    return normalized if normalized in ALLOWED_ROLES else DEFAULT_ROLE

class User:
    """
    User representation model matching database schema.
    """
    def __init__(
        self,
        id: str,
        username: str,
        email: str,
        role: str = DEFAULT_ROLE,
        level: int = 1,
        xp: int = 0,
        coins: int = 1000,
        login_streak: int = 1,
        avatar_url: str | None = None,
        location: str = "Islamabad, PK",
        headline: str = "Creative Technologist & Learner",
        is_verified: bool = False
    ):
        self.id = id
        self.username = username
        self.email = email
        self.role = validate_role(role)
        self.level = level
        self.xp = xp
        self.coins = coins
        self.login_streak = login_streak
        self.avatar_url = avatar_url
        self.location = location
        self.headline = headline
        self.is_verified = is_verified

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "level": self.level,
            "xp": self.xp,
            "coins": self.coins,
            "loginStreak": self.login_streak,
            "avatarUrl": self.avatar_url,
            "location": self.location,
            "headline": self.headline,
            "isVerified": self.is_verified,
        }
