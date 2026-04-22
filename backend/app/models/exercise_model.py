from datetime import datetime


def create_exercise_document(name, category, muscle_group):
    return {
        "name": name.strip(),
        "category": category.lower(),
        "muscle_group": muscle_group.lower(),
        "created_at": datetime.utcnow(),
        "updated_at": datetime.utcnow()
    }