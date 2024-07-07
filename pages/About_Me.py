import streamlit as st

st.header("A little about me!", divider="gray")
with st.expander("Experience"):
    st.write("Podcast | YouTube | E-Commerce | Live Events | Social Media | Curriculum")

    st.write(
        "I have a wide breadth of experience in different B2C areas, and am grateful to have had the opportunity to serve so many customers."
    )

with st.expander("Expertise"):
    st.write(
        """
           I specialize in Streamlit and Tableau Dashboards, ad-hoc analyses, and predictive modeling.

My most recent achievement was a time-series model that we used to help propel a podcast to #1 on the Apple Chart(All-Categories).

Take that Joe Rogan! 😉  
    """
    )


with st.expander("Fun Facts"):
    st.write(
        """
    - My favorite trip was to Thailand where I got to hike with Elephants and swim with Sharks
    - I helped build a church (building) in a small-town in Brazil
    - My secret dream is to become a professional bowler
    """
    )
