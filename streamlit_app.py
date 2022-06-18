import streamlit as st
import utils

st.title('Workout Generator')
description = """
**_DISCLAIMER:_** I am not a personal trainer! Consult your health care professional(s) before taking part in these exercises!

Tired of looking for the right workout? Try this workout generator!
"""
st.markdown(description)

st.sidebar.title("Start here!")
st.sidebar.subheader("Choose your workout")
workout_type = st.sidebar.selectbox(
     'Pick your poison',
     ('Pull', 'Push', 'Legs'))

st.sidebar.subheader("What equipment is available to you?")
st.sidebar.caption("Choose all that apply")
kettlebell = st.sidebar.checkbox('Kettlebell/dumbbell')
bands = st.sidebar.checkbox("Resistance bands")
rings = st.sidebar.checkbox("Gymnastic rings")
bar = st.sidebar.checkbox("Bar")

available_equipment = []
if kettlebell:
    available_equipment.append("kettlebell")
if bands:
    available_equipment.append("resistance band")
if rings:
    available_equipment.append("gymnastic rings")
if bar:
    available_equipment.append("bar")
available_equipment.append("none")

# aesthetic spacing
buffer = st.empty()
buffer.text("\n")

if st.sidebar.button('Generate Workout'):
    if workout_type =="Pull" and len(available_equipment) < 4:
        error_msg = "At least three pieces of equipment are required for a Pull workout. If you don't have any equipment, take a look around your home for viable stand-ins. Here are some ideas: https://www.youtube.com/watch?v=wKlK17aS2T4&ab_channel=ATHLEAN-X%E2%84%A2"
        st.error(error_msg)
    else:
        workout = utils.generate_workout(workout_type, available_equipment)
        st.success(f"Your {workout['name']} Workout was successfully generated!") 
        buffer2 = st.empty()
        buffer2.text("\n")
        st.subheader("Warm-up:")
        st.video(workout["warm up"])
        st.subheader("Abs: ")
        st.video(workout["abs"])
        st.subheader(f'{workout["name"]}:')
        st.write(f'\t\tSets : {workout["sets"]}')
        st.write(f'\t\tReps : {workout["reps"]}')
        for row in workout["primary"].iterrows():
            with st.expander(row[1]["name"]):
                st.write('Sets: 2-4')
                st.write('Reps: 6-10')
                if row[1]["equipment"] != "none":
                    st.write(f'Equipment: {row[1]["equipment"]}')
                st.write(f'Description: {row[1]["description"]}')
                if row[1]["easier"] != "NONE":
                    st.write(f'Easier: {row[1]["easier"]}')
                if row[1]["harder"] != "NONE":
                    st.write(f'Harder: {row[1]["harder"]}')
                if row[1]["link"] != "NONE":
                    st.write(f'Link: {row[1]["link"]}')

st.sidebar.subheader("Philosophy")
philosophy = """
I struggled to get the results I wanted when I began training. Adhering to the following tenets brought me better results. Find what works for you within your goals, with your body and fitness and strength levels. This advice is what worked for me personally, and is not a one-size-fits-all solution.

1. **Quality over quantity**  
    Don't get caught up in counting your reps. Have a goal in mind and get there. Two perfect reps are better than eight poorly executed reps.
2. **Go to exhaustion**  
    I stopped counting reps and push myself to the limit with every set.
3. **Drop sets**   
    Once you reach exhaustion, continue the exercise with an easier variation of the workout or with less weight i.e. Push-ups -> Knee push-ups.
4. **Always warm-up**
    Decrease your chances of injury by properly warming up.

You should **_NOT_** go to exhaustion and do drop sets every workout. Listen to your body and know when you're going too far. Give your body the recovery time it needs.
"""
st.sidebar.write(philosophy)