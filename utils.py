import pandas as pd
import numpy as np
from pathlib import Path
PATH = Path.cwd()

PUSH_TARGET_MUSCLES = ["shoulders", "triceps"]
EXERCISE_FILENAME = "exercises_1.3.csv"
exercises = pd.read_csv(PATH / EXERCISE_FILENAME, header=0)

def generate_workout(workout_type: str, equipment: list) -> dict:
    """ Returns a dict containing workout details"""
    workout = {
        "name": str,
        "warm up": str,
        "abs": str,
        "primary": pd.DataFrame,
        "sets": "2-4",
        "reps": str}
    
    # Warm-up
    # warmups = exercises[exercises["type"] == "Warm-up"]
    # warmup = warmups.sample()
    # warmup.reset_index(inplace=True)
    workout["warm up"] = get_warmup(exercises)
    
    # Abs
    # abs = exercises[exercises["type"] == "Abs"]
    # ab = abs.sample()
    # ab.reset_index(inplace=True)
    # workout["abs"]  = ab.at[0, "link"]
    workout["abs"]  = get_abs(exercises)
    
    # Primary
    # primaries = exercises[exercises["type"] == workout_type]
    # keep_idx = []
    # for row in primaries.iterrows():
    #     exercise_equipment = row[1]["equipment"].split("; ")
    #     for piece in equipment:
    #         if piece in exercise_equipment:
    #             keep_idx.append(row[0])
                
    # unique_keep = list(set(keep_idx))
    # valid_exercises = exercises.iloc[unique_keep]
    # final_exercises = valid_exercises.reset_index().drop(axis=1, labels="index")
    # final_exercises.index += 1
    primary = get_primary(exercises, workout_type=workout_type, equipment=equipment)
    
    if workout_type == "Pull":
        workout["name"] = "Pull Day"
        workout["primary"] =  build_pull_workout(primary).fillna("NONE")
        workout["reps"] = "6-10"
    elif workout_type == "Push":
        workout["name"] = "Push Day"
        workout["primary"] =  build_push_workout(primary).fillna("NONE")
        workout["reps"] = "6-10"
    else:
        workout["name"] = "Leg Day"
        workout["primary"] =  build_leg_workout(primary).fillna("NONE")
        workout["reps"] = "8-12"
    return workout

def get_warmup(exercise_list: pd.DataFrame) -> str:
    warmups = exercise_list[exercise_list["type"] == "Warm-up"]
    warmup = warmups.sample()
    warmup.reset_index(inplace=True)
    return warmup.at[0,"link"]

def get_abs(exercise_list: pd.DataFrame) -> str: # Get it? Get abs!
    abs = exercise_list[exercise_list["type"] == "Abs"]
    ab = abs.sample()
    ab.reset_index(inplace=True)
    return ab.at[0, "link"]  
    
def get_primary(exercise_list: pd.DataFrame, workout_type: str, equipment: list) -> pd.DataFrame:
    primaries = exercise_list[exercise_list["type"] == workout_type]
    keep_idx = []
    for row in primaries.iterrows():
        exercise_equipment = row[1]["equipment"].split("; ")
        for piece in equipment:
            if piece in exercise_equipment:
                keep_idx.append(row[0])
                
    unique_keep = list(set(keep_idx))
    valid_exercises = exercises.iloc[unique_keep]
    final_exercises = valid_exercises.reset_index().drop(axis=1, labels="index")
    final_exercises.index += 1
    return final_exercises

def build_pull_workout(exercise_list: pd.DataFrame) -> pd.DataFrame:
    primary = exercise_list[exercise_list["role"] == "primary"].sample()
    secondary = exercise_list[exercise_list["role"] == "secondary"].sample(n=3)
    pull = pd.concat([primary, secondary], axis=0).reset_index().drop(axis=1, labels="index")
    pull.index += 1
    return pull

def build_push_workout(exercise_list: pd.DataFrame) -> pd.DataFrame:
    primary = exercise_list[exercise_list["role"] == "primary"].sample(2)
    target_muscle = PUSH_TARGET_MUSCLES[np.random.randint(0,high=1)]
    secondary = exercise_list.loc[(exercise_list.role == "secondary") & (exercise_list.target == target_muscle)].sample(n=2)
    push = pd.concat([primary, secondary], axis=0).reset_index().drop(axis=1, labels="index")
    push.index += 1
    return push

def build_leg_workout(exercise_list: pd.DataFrame) -> pd.DataFrame:
    primary = exercise_list[exercise_list["role"] == "primary"].sample()
    secondary = exercise_list[exercise_list["role"] == "secondary"].sample(n=3)
    legs = pd.concat([primary, secondary], axis=0).reset_index().drop(axis=1, labels="index")
    legs.index += 1
    return legs
