import streamlit as st

# 1) Titles & Text

# st.title → Display a big title at the top of the page
st.title("My App Title")

# st.header → Display a section header
st.header("This is a header")

# st.subheader → Display a smaller header
st.subheader("This is a subheader")

# st.markdown → Write text using Markdown formatting (bold, italic, etc.)
st.markdown("**Bold Text**, *Italic Text*, [Link](https://streamlit.io)")

# st.text → Display plain text (no formatting)
st.text("This is just plain text")

# st.write → Flexible function: can display text, numbers, dicts, lists, DataFrames, etc.
st.write("Hello, World!", 123, {"a": 1, "b": 2})

# st.code → Display a code block with optional syntax highlighting
st.code("print('Hello from code block')", language="python")

# st.divider → Horizontal line to separate sections
st.divider()


# 2) User Input Widgets

# st.text_input → Get text input from user
name = st.text_input("Enter your name:")

# st.slider → Create a slider for numbers
age = st.slider("Select Age:", 1, 100, 25)   # (label, min, max, default)

# st.multiselect → Allow user to pick multiple options
hobbies = st.multiselect("Pick hobbies:", ["Music", "Sports", "Coding"])

# st.checkbox → Checkbox (True/False)
agree = st.checkbox("I agree")

# st.radio → Radio buttons (choose only one option)
gender = st.radio("Select gender:", ["Male", "Female", "Other"])


# 3) File Upload & Images

# st.file_uploader → Upload files (images, CSVs, etc.)
file = st.file_uploader("Upload File", type=["jpg", "png", "csv"])

# st.image → Display an image
st.image(file, caption="Uploaded Image", use_column_width=True)


# 4) Buttons & Actions

# st.button → Button that triggers an action when clicked
if st.button("Click Me"):
    st.write("Button clicked!")

# st.balloons → Fun animation (balloons falling down)
st.balloons()


# 5) Messages & Alerts

# st.success → Green success message
st.success("Success! Operation completed.")

# st.error → Red error message
st.error("Error! Something went wrong.")

# st.warning → Yellow warning message
st.warning("Warning! Be careful.")

# st.info → Blue info message
st.info("Information message.")


# 6) Sidebar Navigation

# st.sidebar.title → Add title in sidebar
st.sidebar.title("Navigation Menu")

# st.sidebar.selectbox → Dropdown in sidebar
option = st.sidebar.selectbox("Choose Page:", ["Home", "About"])


# 7) Layout Options

# st.columns → Split page into columns
col1, col2 = st.columns(2)
col1.write("This is column 1")
col2.write("This is column 2")

# st.expander → Collapsible section
with st.expander("See More"):
    st.write("Hidden content until expanded.")


# 8) Progress & Status

# st.progress → Progress bar
import time
progress = st.progress(0)
for i in range(100):
    time.sleep(0.01)
    progress.progress(i+1)
