#!/usr/bin/env python
# coding: utf-8

# In[6]:


import pandas as pd
import streamlit as st
import pickle
import sklearn
st.title('IPL WIN PREDICTOR')
teams = ['Royal Challengers Bangalore',
 'Kings XI Punjab',
 'Mumbai Indians',
 'Kolkata Knight Riders',
 'Rajasthan Royals',
 'Chennai Super Kings',
 'Sunrisers Hyderabad',
 'Delhi Capitals']

venue = [
        'Feroz Shah Kotla',
       'Wankhede Stadium', 'Eden Gardens', 'Sawai Mansingh Stadium',
       'Rajiv Gandhi International Stadium, Uppal',
       'MA Chidambaram Stadium, Chepauk', 'Dr DY Patil Sports Academy',
       'Newlands', "St George's Park", 'Kingsmead', 'SuperSport Park',
       'Buffalo Park', 'New Wanderers Stadium', 'De Beers Diamond Oval',
       'OUTsurance Oval', 'Brabourne Stadium',
       'Sardar Patel Stadium, Motera', 'Barabati Stadium',
       'Vidarbha Cricket Association Stadium, Jamtha',
       'Himachal Pradesh Cricket Association Stadium',
       'Dr. Y.S. Rajasekhara Reddy ACA-VDCA Cricket Stadium',
       'Subrata Roy Sahara Stadium',
       'Shaheed Veer Narayan Singh International Stadium',
       'JSCA International Stadium Complex', 'Sheikh Zayed Stadium',
       'Sharjah Cricket Stadium', 'Dubai International Cricket Stadium',
       'Maharashtra Cricket Association Stadium',
       'Punjab Cricket Association IS Bindra Stadium, Mohali',
       'M.Chinnaswamy Stadium', 'Holkar Cricket Stadium']

decision = ['bat', 'field']

pipe = pickle.load(open('pipe.pkl','rb'))

col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox('Select the batting team', sorted(teams))

with col2:
    bowling_team = st.selectbox('Select the bowling team', sorted(teams))

    # Validate that batting_team and bowling_team are different
    if bowling_team == batting_team:
        st.warning("Bowling team cannot be the same as batting team. Please choose a different team.")
        st.stop()  # Stop execution if teams are the same
selected_venue = st.selectbox('Select the venue', sorted(venue))

target = st.number_input('Target',max_value = 300)
if  target> 300:
    st.warning("Invalid target.")
    st.stop()
toss_teams = [str(batting_team)  , str(bowling_team)]


col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input('Score', max_value=300)

with col4:
    overs = st.number_input('Overs Completed', max_value=20)

with col5:
    wickets = st.number_input('Number of Wickets Gone', max_value=10)

# Validate score, overs, and wickets
if score >= target:
    st.warning("Score cannot be greater or equal to target.")
    st.stop()

if overs > 20:
    st.warning("Overs completed cannot be greater than 20.")
    st.stop()

if wickets > 10:
    st.warning("Number of wickets gone cannot be greater than 10.")
    st.stop()

col6,col7 = st.columns(2)
with col6:
    toss_winner = st.selectbox('Toss Winner',sorted(toss_teams))
with col7:
    toss_decision = st.selectbox('Toss Decision' ,decision)


if st.button("Predict"):
    runs_to_win = target-score
    balls_left = 120-(overs*6)
    wickets = 10 - wickets
    curr = score/overs
    rrr = (runs_to_win*6)/(balls_left)




    input_df = pd.DataFrame(
        {'batting_team':[batting_team],
         'bowling_team':[bowling_team],
         'venue':[selected_venue],
         'runs_to_win': [runs_to_win],
         'balls_left':[balls_left],
         'wickets_left' : [wickets],
         'total_runs_x':[target],
         'curr':[curr],
         'rrr':[rrr],
         'toss_decision': [toss_decision],
         'toss_winner':[toss_winner]
        }
    )


    result = pipe.predict_proba(input_df)
    loss = result[0][0]
    win = result[0][1]
    st.header(batting_team+"- "+ str(round(win*100))+"%")
    st.header(bowling_team+"- "+ str(round(loss*100))+"%")




# In[ ]:




