import streamlit as st
import random

def generate_joke():
    jokes = [
        "Why did the scarecrow win an award? Because he was outstanding in his field!",
        "Why don't scientists trust atoms? Because they make up everything!",
        "What do you call fake spaghetti? An impasta!",
        "Why couldn't the bicycle stand up by itself? It was two-tired!",
        "What did one hat say to the other? You stay here, I'll go on ahead!",
        "Why did the tomato turn red? Because it saw the salad dressing!",
        "Why was the math book sad? Because it had too many problems!",
        "What do you get when you cross a snowman and a vampire? Frostbite!",
        "What did one ocean say to the other ocean? Nothing, they just waved!",
        "Why don't skeletons fight each other? They don't have the guts!"
    ]
    return random.choice(jokes)

st.title("Funny Joke Generator")

if st.button("Tell me a joke!"):
    joke = generate_joke()
    st.write(joke)
