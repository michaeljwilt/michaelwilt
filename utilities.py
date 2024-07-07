import streamlit as st


def build_page_navigation():
    pages = {
        "Home": [
            st.Page(
                "pages/HomePage.py",
                title="HomePage",
                icon=":material/home:",
                default=True,
            ),
        ],
        "Projects": [
            st.Page(
                "pages/Biblical_Festivals.py",
                title="Biblical Festivals",
                icon=":material/synagogue:",
            ),
            st.Page(
                "pages/Podcast_Dashboard.py",
                title="Podcast Dashboard",
                icon=":material/podcasts:",
            ),
            # st.Page(
            #     "pages/Prophet.py",
            #     title="Prophet",
            #     # icon=":material/meta:",
            # ),
        ],
        "About": [
            st.Page(
                "pages/About_Me.py",
                title="About Me",
                icon=":material/info:",
            )
        ],
    }

    pg = st.navigation(pages)
    pg.run()
