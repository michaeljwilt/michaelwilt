import streamlit as st


# -------------------------CSS-------------------------#
# open/create css object
with open("css/styles.css") as f:
    css = f.read()
# apply css to page
st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

    /* Apply the font to the body */
    body {
        font-family: 'Inter', sans-serif;
        transition: background 0.5s ease;
    }
    body:hover {
        background: linear-gradient(to right, #ff7e5f, #feb47b);
    }
    .large-header {
        padding-bottom: 0px;
    }
    p {
        font-size: 18px;
    }

    /* Additional custom CSS */
    </style>
    """,
    unsafe_allow_html=True,
)


_, col1, col2 = st.columns([0.25, 1, 1])

with col1:
    st.markdown(
        """
    <h1 class="large-header">Michael Wilt</h1>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    <h2 style="padding-bottom:0px;">Data Scientist</h2>
    """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
    <style>
    .gray-text {
        color: #738099;
        font-size: 16px;
        padding-top: 0px;
        
    }
    .link-style {
        color: #d8dfee; /* Link color */
        text-decoration: none; /* Remove underline */
    }
    .link-style:hover {
        text-decoration: underline; /* Underline on hover */
    }
    </style>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p class="gray-text">I build data products to drive actionable <br> insights and strategic growth.</p>',
        unsafe_allow_html=True,
    )
    st.write("")
    st.page_link(
        "pages/Podcast_Dashboard.py",
        label="Project #1",
        icon=":material/podcasts:",
    )
    st.page_link(
        "pages/Biblical_Festivals.py",
        label="Project #2",
        icon=":material/synagogue:",
    )
    st.page_link("pages/About_Me.py", label="About Me", icon=":material/info:")

    subcol1, subcol2, subcol3, _ = st.columns([1, 1, 1, 5])


with col2:

    st.markdown(
        """
        <p class="gray-text">
            Back in 2022, I went back to school to study Data Science. During my tenure in school, I was hired to help teach in that same Data Science program.
            Fast forward to today, I've had the opportunity to build data products for an <b style="color: #d8dfee;"> accredited college</b>, 
        a <b style="color: #d8dfee;">podcast and youtube network</b>, and 
        a <b style="color: #d8dfee;">medium-sized B2C corporation</b>.
    </p>
            """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <p class="gray-text">
            My main focuses these days is building robust data products, primarily utilizing <b style="color: #d8dfee;">Streamlit</b>'s robust interface.
            I most enjoy pushing the bourndaries of what we typically think of data science and finding ways to learn about and implement more AI applications 
            into everyday business opoortunities. A few of my major accomplishments so far are: <b style="color: #d8dfee;">helping propel a podcast to #1 on the Apple charts</b> using predictive modeling,
            and assisting in efforts that led to a <b style="color: #d8dfee;">social media growth of 8 Million+ followers.</b>
        </p>
            """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <p class="gray-text">
            
        </p>
            """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div style="text-align: center; padding-bottom:0px;">
        <h1>My Services</h1>
        <hr style="border-color: gray;">
    </div>
    """,
    unsafe_allow_html=True,
)
# st.header("My Services", divider="gray")

col1, col2, col3 = st.columns(3)


with col1:
    st.markdown(
        """
    <div style="text-align: center; padding-bottom:0px;">
        <h3>Consulting</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.write(
        """
        Looking for a third party perspective? I’ll work with your teams and leaders to assess their data processes and identify areas for improvement.
        """
    )

with col2:
    st.markdown(
        """
    <div style="text-align: center; padding-bottom:0px;">
        <h3>Ad-Hoc Projects</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.write(
        """
        Navigating through your backlog can be challenging, but fear not—I'm here to join forces with you in advancing projects across your board.
        """
    )

with col3:
    st.markdown(
        """
    <div style="text-align: center; padding-bottom:0px;">
        <h3>Contracting</h3>
    </div>
    """,
        unsafe_allow_html=True,
    )
    st.write(
        """
        Whether short-term or long-term, I'm here to partner with your team in advancing your analytics capabilities.
        """
    )
