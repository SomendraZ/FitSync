from datetime import datetime, UTC


def create_user_document(email, hashed_password, username):
    now_utc = datetime.now(UTC)

    return {
        "email": email,
        "password": hashed_password,
        "username": username,
        "created_at": now_utc,
        "updated_at": now_utc
    }