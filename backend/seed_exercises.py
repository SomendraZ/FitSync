from app.db import db

# Prevent duplicate seeding
if db.exercises.count_documents({}) > 0:
    print("✅ Exercises already exist. Skipping seeding.")
else:
    db.exercises.insert_many([

    # 🔴 PUSH (Chest, Shoulders, Triceps)
    {"name": "Push Up", "category": "push", "muscle_group": "chest"},
    {"name": "Bench Press", "category": "push", "muscle_group": "chest"},
    {"name": "Incline Bench Press", "category": "push", "muscle_group": "chest"},
    {"name": "Decline Bench Press", "category": "push", "muscle_group": "chest"},
    {"name": "Chest Fly", "category": "push", "muscle_group": "chest"},
    {"name": "Dumbbell Press", "category": "push", "muscle_group": "chest"},

    {"name": "Shoulder Press", "category": "push", "muscle_group": "shoulders"},
    {"name": "Arnold Press", "category": "push", "muscle_group": "shoulders"},
    {"name": "Lateral Raise", "category": "push", "muscle_group": "shoulders"},
    {"name": "Front Raise", "category": "push", "muscle_group": "shoulders"},

    {"name": "Tricep Dips", "category": "push", "muscle_group": "triceps"},
    {"name": "Tricep Pushdown", "category": "push", "muscle_group": "triceps"},
    {"name": "Overhead Tricep Extension", "category": "push", "muscle_group": "triceps"},

    # 🔵 PULL (Back, Biceps)
    {"name": "Pull Up", "category": "pull", "muscle_group": "back"},
    {"name": "Chin Up", "category": "pull", "muscle_group": "back"},
    {"name": "Lat Pulldown", "category": "pull", "muscle_group": "back"},
    {"name": "Barbell Row", "category": "pull", "muscle_group": "back"},
    {"name": "Seated Row", "category": "pull", "muscle_group": "back"},
    {"name": "Deadlift", "category": "pull", "muscle_group": "back"},

    {"name": "Bicep Curl", "category": "pull", "muscle_group": "biceps"},
    {"name": "Hammer Curl", "category": "pull", "muscle_group": "biceps"},
    {"name": "Preacher Curl", "category": "pull", "muscle_group": "biceps"},

    # 🟢 LEGS
    {"name": "Squat", "category": "legs", "muscle_group": "legs"},
    {"name": "Lunges", "category": "legs", "muscle_group": "legs"},
    {"name": "Leg Press", "category": "legs", "muscle_group": "legs"},
    {"name": "Leg Extension", "category": "legs", "muscle_group": "legs"},
    {"name": "Leg Curl", "category": "legs", "muscle_group": "legs"},
    {"name": "Calf Raise", "category": "legs", "muscle_group": "calves"},
    {"name": "Bulgarian Split Squat", "category": "legs", "muscle_group": "legs"},

    # 🟡 ABS / CORE
    {"name": "Crunches", "category": "core", "muscle_group": "abs"},
    {"name": "Plank", "category": "core", "muscle_group": "abs"},
    {"name": "Leg Raises", "category": "core", "muscle_group": "abs"},
    {"name": "Russian Twist", "category": "core", "muscle_group": "abs"},
    {"name": "Mountain Climbers", "category": "core", "muscle_group": "abs"},
    {"name": "Bicycle Crunch", "category": "core", "muscle_group": "abs"},

    # 🟣 CARDIO
    {"name": "Running", "category": "cardio", "muscle_group": "full_body"},
    {"name": "Cycling", "category": "cardio", "muscle_group": "legs"},
    {"name": "Jump Rope", "category": "cardio", "muscle_group": "full_body"},
    {"name": "Burpees", "category": "cardio", "muscle_group": "full_body"},
    {"name": "Jumping Jacks", "category": "cardio", "muscle_group": "full_body"},
    {"name": "High Knees", "category": "cardio", "muscle_group": "legs"},

    # 🟤 FULL BODY
    {"name": "Clean and Press", "category": "full_body", "muscle_group": "full_body"},
    {"name": "Kettlebell Swing", "category": "full_body", "muscle_group": "full_body"},
    {"name": "Thrusters", "category": "full_body", "muscle_group": "full_body"}

    ])

    print("🔥 Exercises seeded successfully!")