def validate_entry(habit, mood, energy):
    if not habit or habit.strip() == "":
        raise ValueError("Habit name cannot be empty.")

    if not isinstance(mood, int) or not 1 <= mood <= 5:
        raise ValueError("Mood must be an integer from 1–5.")

    if not isinstance(energy, int) or not 1 <= energy <= 5:
        raise ValueError("Energy must be an integer from 1–5.")
