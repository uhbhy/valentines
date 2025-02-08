import streamlit as st
import time
from PIL import Image


def main():
    # Custom Styling for Background Color
    st.markdown("""
        <style>
        .big-heart {
            font-size: 100px;
            text-align: center;
        }
        
        /* Set the background color for the whole page */
        [data-testid="stAppViewContainer"] {
            background-color: #C790D8;
        }
        </style>
    """, unsafe_allow_html=True)

    # Title with Heart Emoji
    st.markdown("<h1 style='text-align: center;'>❤️ Hey Love! ❤️</h1>", unsafe_allow_html=True)

    # Animated Heart
    st.markdown("<p class='big-heart'>💖</p>", unsafe_allow_html=True)

    # Display button immediately
    reveal = st.button("I've been meaning to ask you something for a while.........💌")

    if 'revealed' not in st.session_state:
        st.session_state.revealed = False

    if reveal:
        st.session_state.revealed = True

    if st.session_state.revealed:
        st.markdown(
            """
            <h2 style='text-align: center;'>
            You are my entire universe 🌌
            and I can't imagine this Valentine's Day without you! 💕
            </h2>
            <h3 style='text-align: center;'>Will you be my Valentine? 🥰</h3>
            """, unsafe_allow_html=True
        )
        
        # Yes-only buttons
        col1, col2 = st.columns(2)
        with col1:
            if st.button("Yes! 💖"):
                st.success("Yay! I can't wait to celebrate with you! 🎉🥰")
                st.balloons()
        with col2:
            if st.button("Absolutely! 💘"):
                st.success("I knew it! You're the best! 😘")
                st.snow()
                
        # Bonus: Cute AI-generated poem
        st.markdown(
            """
            ---
            **A Little Poem for You** 🌹
            
            Roses are red, violets are blue,  
            My world is perfect, because you call me PUPU.💕
            """
        )

if __name__=="__main__":
    main()