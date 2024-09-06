import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/brain.jpg")
img_lottie_animation = Image.open("images/cat.jpg")

# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi :wave:")
    st.title("This is the official page of xyz thing🌏")
    st.write(
        "This is just a weird webpage. I don't know why I am making this, LOLzz. My main purpose is to make a webapp and stuff!💻 "
    )
    st.write("I know a webpage for you 🫵")
    st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            "Nothing.... Hey I found a website where you will get to know about human brain, love etcetera etcetera "
        )
        st.write("Ps-Basically answer to life,the universe, and everthing🤫")
        st.write("[YouTube Channel >](https://www.youtube.com/watch?v=xvFZjo5PgG0)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_contact_form)
    with text_column:
        st.subheader("i am bored")
        st.write(
            """
           (some random stuff) Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=xvFZjo5PgG0)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("woahh")
        st.write(
            """
           Classy Cat 🥰"""
        )
        st.markdown("[Watch Video...](https://www.youtube.com/watch?v=xvFZjo5PgG0)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/suhail17mohammad@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()