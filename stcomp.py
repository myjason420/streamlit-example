import streamlit as st
import streamlit.components.v1 as components

# embed streamlit docs in a streamlit app
components.iframe(src="https://api.digitallocker.gov.in/public/oauth2/1/authorize?response_type=code&client_id=1400793F&redirect_uri=https://www.godigit.com/callback&state=codex1234",width=250, height=250, scrolling=True)
