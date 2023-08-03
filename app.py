import streamlit as st
import utils # noqa WE IMPORT THIS to trigger django setup only once

from django.contrib.auth.models import User

st.write(list(User.objects.all()))

x = st.slider("AAAA", 0, 100, 27)

st.write(x**2)


