import psycopg2
import streamlit as st

from core.scripts import database_repository, utils

if "user_id" not in st.session_state:
    st.session_state.user_id = ""

if "page" not in st.session_state:
    st.session_state.page = "main"

if "conn" not in st.session_state:
    st.session_state.conn = database_repository.db_connection()

# database_repository.init_db()  # can comment out now, since it already exists...


# Emoticons can be copied from here: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
# define pages
main_page = st.Page(
    "core/pages/main_page.py", title="Start Page", icon="🏚️"
)
authentication_page = st.Page(
    "core/pages/authentication_page.py", title="Log In", icon="🎟️", url_path="authentication", default=True
)
admin_page = st.Page(
    "core/pages/admin_page.py", title="Admin Area", icon="💻"
)
logout_page = st.Page(
    "core/pages/logout_page.py", title="Log Out", icon="↩️"
)

# Task Pages 
implicit_meaning_start_page = st.Page(
    "implicit_meaning_task/pages/introduction_page.py", title="Implicit Meaning Task Intro",  icon="📙", url_path="implicit_task_intro" 
)
implicit_meaning_qualification_page = st.Page(
    "implicit_meaning_task/pages/qualification_page.py", title="Qualification", icon="🔑"
)
implicit_meaning_annotation_page = st.Page(
    "implicit_meaning_task/pages/annotation_page.py", title="Annotation", icon="✏️"
)


# Create navigation bar

if st.session_state.user_id == "admin":
    pg = st.navigation(
        {
            "Home": [main_page, admin_page, logout_page],
        }
    )
elif st.session_state.user_id:
    available_pages = {
        "Home": [main_page]
    }
    if utils.authenticate_id("implicit_meaning_task", st.session_state.user_id):
        available_pages["Implicit Meaning Task"] = [implicit_meaning_start_page, implicit_meaning_qualification_page, implicit_meaning_annotation_page]

    available_pages["Other"] = [logout_page]

    pg = st.navigation(available_pages)

else:
    pg = st.navigation(
        {
        "Home": [main_page, authentication_page],
        "Task Previews": [implicit_meaning_start_page]
        }

    )

try:
    pg.run()
except (psycopg2.InterfaceError, psycopg2.OperationalError) as e:
    st.markdown("# Your session was cancelled, likely due to prolonged inactivity. Please log out, then log in again.")
    print(e)