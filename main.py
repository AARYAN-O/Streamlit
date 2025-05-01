import streamlit as st

st.title("title")
st.header("header")
st.subheader("subheader")
st.text("text")
st.markdown("**Bold**")
st.markdown("_Italic_") #Note : The italics use only single underscores on both of its sides.
st.markdown("`code`")
st.code("print('language specific code block')",language="python") #st.code() works for languages like python , sql , js , html , css,
#json,yaml , Markdown, bash/shell , jaa, cpp, c, r, go, php,rust
# In streamlit , indentation also matters
st.image("wallpaper.jpeg", caption="Mountain Image", width=300)
st.audio("indian-bollywood-hindi-song-background-music-294105.mp3")
st.write("Demo Aaryan Audio")
st.video("https://youtu.be/syFZfO_wfMQ?si=2gcx0w9yyn6V8GXW") #Here we have used a youtube video url. But we can also use local video files
st.write("Demo Aaryan Video")

# Does streamlit allow using html ? 
# Yes , we can use html components inside st.markdown() and for full html + js embeds , we can use st.components.v1.html()
# We cannot directly run javascript inside st.markdownn()
# For that we can import : import streamlit.components.v1 as components

name=st.text_input("Hi Aaryan , Please enter your input value")
age=st.number_input("Hi Aaryan , Please enter your age") #default

age=st.number_input("Hi Aaryan, Please enter your age again",18,100,20)

color=st.color_picker("Hi Aaryan, Pick a Color")

selected_option=st.selectbox("Hi Aaryan , What would you like to eat ",["Paneer Butter Masala","Kadhai Paneer"])

csv_uploader=st.file_uploader("Upload CSV")
png_uploader=st.file_uploader("Upload PNG")

# if csv_uploader:
#     import pandas as pd 
#     pd.read_csv(csv_uploader)

status=st.button("Click this button")

if status:
    st.success("Button Clicked")

st.write("Creating Columns")

col1, col2 = st.columns(2)
col1.metric("Temp", "70°F", "+2°F")
col2.metric("Temp","36 degree celcius","Hi")


st.write("Expander")
with st.expander("See more"):
    st.write("This is hidden content revealed when expanded.")


with st.sidebar:
    st.title("Navigation")
    radio_state=st.radio("Go to", ["Home", "Settings"])

if radio_state=='Home':
    st.write("Home is clicked")
elif radio_state=='Settings':
    st.write("Settings is clicked")


import pandas as pd
import numpy as np

df = pd.DataFrame({
    "x": np.random.randn(100),
    "y": np.random.randn(100)
})


st.title("Pandas DataFrame")
st.dataframe(df)
# This is interactive and it can be scrolled.
# We can use this for larger datasets
# We can even download the dataframe here



st.title("Table")
st.table(df.head())
# This is static and should be used for smaller dataframes.

st.title("Charts")

st.write("Line Chart")
st.line_chart(df)

st.write("Bar Chart")
st.bar_chart(df)

st.title("Sliders")
# Sliders are used to make the charts interactive. We can slide the axes to change the charts
st.slider("Slide the slider from 0 to 100",0,100,10,5)
# 0--> mn value
# 100 --> max value
# 10 --> starting value of slider
# 5 --> step 


st.title("Using matplotlib")
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6])
st.pyplot(fig)



fig, ax = plt.subplots()
ax.plot([1, 2, 3], [4, 5, 6], marker='o', linestyle='--', color='green')
ax.set_title("Custom Line Plot")
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
st.pyplot(fig)
