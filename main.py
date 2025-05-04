# Code for learning basics of streamlit


import streamlit as st

# Displays a big title at the top of the web app.
# Rendered as an <h1> tag in HTML.
st.title("title")

# Displays a header — slightly smaller than a title.
# Used to divide your app into sections.
st.header("header")

# Displays a subheader — smaller than a header.
# Used to create subsections.
# Renders as <h3>.
st.subheader("subheader")

# Shows plain text (no formatting).
# Use this for general information or instructions.
st.text("text")

# Displays formatted text using Markdown syntax.
# Markdown allows you to style text easily.
# **Bold** → Bold
# _Italic_ → Italic
# `code` → code
st.markdown("**Bold**")
st.markdown("_Italic_") #Note : The italics use only single underscores on both of its sides.
st.markdown("`code`")
st.code("print('language specific code block')",language="python") #st.code() works for languages like python , sql , js , html , css,
#json,yaml , Markdown, bash/shell , jaa, cpp, c, r, go, php,rust
# In streamlit , indentation also matters

# Media

# Displays an image on the Streamlit app.
# "image.jpg" is the path to the image file (can be local or a URL).
# caption="Nice Image" adds a label below the image.
# width=300 sets the display width in pixels (optional).
st.image("wallpaper.jpeg", caption="Mountain Image", width=300)

# Embeds an audio player in the app.
# "audio.mp3" is the path to the audio file (can be local or URL).
# Allows users to play, pause, and control volume.
# Use Cases:
# Playing music, sound effects, voice recordings, etc.
st.audio("indian-bollywood-hindi-song-background-music-294105.mp3")

# writes to the app
st.write("Demo Aaryan Audio")

# "video.mp4" is the video file path or URL.
# Users can play, pause, seek, and control playback speed.
# Supports:
# Local files (.mp4, .mov, etc.)
# YouTube and other video URLs.
st.video("https://youtu.be/syFZfO_wfMQ?si=2gcx0w9yyn6V8GXW") #Here we have used a youtube video url. But we can also use local video files
st.write("Demo Aaryan Video")

# Does streamlit allow using html ? 
# Yes , we can use html components inside st.markdown() and for full html + js embeds , we can use st.components.v1.html()
# We cannot directly run javascript inside st.markdownn()
# For that we can import : import streamlit.components.v1 as components


# Widgets

# Creates a text box where users can type in a string.
# Label: Enter your name
# The user's input is stored in the name variable.
# Example:
# [ Enter your name:  John ]
name=st.text_input("Hi Aaryan , Please enter your input value")

# Creates a numeric input box for entering numbers.
# Label: Your age
# Parameters:
# 0: minimum value
# 100: maximum value
# 25: default value shown initially
# Stores the selected number in age.
# Example:
# [ Your age: 25 ]
age=st.number_input("Hi Aaryan , Please enter your age") #default

age=st.number_input("Hi Aaryan, Please enter your age again",18,100,20)


# Provides a color selection tool.
# Label: Pick a color
# Returns the selected color as a hex string (e.g., #FF0000).
# Example:
# [Color picker input that opens a color palette]
color=st.color_picker("Hi Aaryan, Pick a Color")


# Creates a drop-down menu.
# Label: Choose one
# Options: "Apple", "Banana", "Cherry"
# Returns the selected item in option.
# Example:
# [ Apple ▼ ]

selected_option=st.selectbox("Hi Aaryan , What would you like to eat ",["Paneer Butter Masala","Kadhai Paneer"])

# Allows the user to upload a file from their system.
# Label: Upload CSV
# Typically used for .csv, .xlsx, etc.
# Returns a file-like object or None.
# Common Use:
# if uploaded is not None:
#     import pandas as pd
#     df = pd.read_csv(uploaded)
#     st.write(df.head())
csv_uploader=st.file_uploader("Upload CSV")
png_uploader=st.file_uploader("Upload PNG")

# if csv_uploader:
#     import pandas as pd 
#     pd.read_csv(csv_uploader)

# Renders a button with the label “Click Me”.
# Returns True when the user clicks it.
# st.success("You clicked!")
# This runs only when the button is clicked.
# Displays a green success message saying “You clicked!”
# Output Behavior:
# Initial state: shows a button.
# After click: shows the message under the button like a success alert.

status=st.button("Click this button")

if status:
    st.success("Button Clicked")

st.write("Creating Columns")


# Columns

# The st.metric function in Streamlit allows you to display a metric in a big, bold font, with an optional indicator of how the metric changed1.
col1, col2 = st.columns(2)
col1.metric("Temp", "70°F", "+2°F")
col2.metric("Temp","36 degree celcius","Hi")

# Expander

# Output 

# [+] See more  (collapsed)

# [-] See more
#     Here is hidden content.  (expanded)

st.write("Expander")
with st.expander("See more"):
    st.write("This is hidden content revealed when expanded.")



# st.sidebar: Adds content to the sidebar panel on the left.
# with st.sidebar:: Lets you group multiple elements into the sidebar.
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


# Table
st.title("Table")
st.table(df.head())
# This is static and should be used for smaller dataframes.

st.title("Charts")

st.write("Line Chart")

# Creates a line chart for all numeric columns.
# By default, plots x and y values with index on the x-axis.
st.line_chart(df)

st.write("Bar Chart")

# Plots a bar chart of just the "x" column.

# Useful for seeing distributions or comparisons.
st.bar_chart(df)


st.title("Sliders")

# Sliders are used to make the charts interactive. We can slide the axes to change the charts
# Let users filter data with a slider and show charts only after clicking a button.
st.slider("Slide the slider from 0 to 100",0,100,10,5)
# 0--> mn value
# 100 --> max value
# 10 --> starting value of slider
# 5 --> step 

# Renders the Matplotlib plot inside your Streamlit app.
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
