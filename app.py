import streamlit as st 
import random

st.write("Welcome to my first Project")
st.title("Rock-Paper-Scissors Game")

#selectingbox for user
player = st.selectbox(
    "Choose your move : ",
    ["Rock", "Paper", "Scissors"]
)

#there is no while loop as whenever user taps play button it will autommatically run
if st.button("PLAY"): 
    computer = random.choice(["Rock", "Paper", "Scissors"])
    
    #showing choices
    st.write("You Chose : " + player)
    st.write("Computer Chose : " + computer)

    #winner logic
    if player == computer : 
        st.info("Match Tied!")
        st.toast("Try Again!")
    elif(player == "Rock" and computer == "Scissors") or \
    (player == "Paper" and computer == "Rock") or \
    (player == "Scissors" and computer == "Paper") : 
        st.success("You Won!")
        st.balloons()
    else : 
        st.error("Computer Won!")
        st.toast("Try Again!")
