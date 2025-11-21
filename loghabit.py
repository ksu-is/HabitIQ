import pandas as pd
from datetime import datetime

def log_habit(habit, mood, energy):
    validate_entry(habit, mood, energy)
    
    df = pd.DataFrame([{
        "habit": habit,
        "mood": mood,
        "energy": energy,
        "timestamp": datetime.now()
    }])

    df.to_csv("habit_data.csv", mode="a", header=False, index=False)
