import streamlit as st
import pickle
import pandas as pd

teams = ['Sunrisers Hyderabad',
 'Mumbai Indians',
 'Royal Challengers Bangalore',
 'Kolkata Knight Riders',
 'Kings XI Punjab',
 'Chennai Super Kings',
 'Rajasthan Royals',
 'Delhi Capitals']

cities = ['Hyderabad', 'Bangalore', 'Mumbai', 'Indore', 'Kolkata', 'Delhi',
       'Chandigarh', 'Jaipur', 'Chennai', 'Cape Town', 'Port Elizabeth',
       'Durban', 'Centurion', 'East London', 'Johannesburg', 'Kimberley',
       'Bloemfontein', 'Ahmedabad', 'Cuttack', 'Nagpur', 'Dharamsala',
       'Visakhapatnam', 'Pune', 'Raipur', 'Ranchi', 'Abu Dhabi',
       'Sharjah', 'Mohali', 'Bengaluru']

pipe = pickle.load(open('pipe.pkl','rb'))
st.title('🏏 IPL Winning 🏆 Predictor 🏏 ')

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('⚔ Select the batting team 🏏',sorted(teams))
with col2:
    bowling_team = st.selectbox('⚔ Select the bowling team ⚾',sorted(teams,reverse=True))

selected_city = st.selectbox('🌍 Select host city 🌍',sorted(cities))

col3,col4 = st.columns(2)
with col3:
    target = st.number_input(label='🎯 Target 🎯',min_value=0)
    
with col4:
    score = st.number_input('Current Score',min_value=0)

overs=st.slider(label="Overs Completed ",min_value=0,max_value=20)
wickets = st.slider(label="Wickets ",min_value=0,max_value=10)


if st.button('Predict Probability 🔥'):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    wickets = 10 - wickets
    crr = score/overs
    st.text(f"The Current Run Rate is ==> {crr}")
    rrr = (runs_left*6)/balls_left
    st.text(f"The Required Run Rate is ==> {rrr}")

    input_df = pd.DataFrame({'batting_team':[batting_team],'bowling_team':[bowling_team],'city':[selected_city],'runs_left':[runs_left],'balls_left':[balls_left],'wickets':[wickets],'total_runs_x':[target],'crr':[crr],'rrr':[rrr]})

    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.subheader(batting_team + "=> " + str(round(win*100)) + "%  🎉🏆")
    st.subheader(bowling_team + "=> " + str(round(loss*100)) + "%  🏆🎊")
    