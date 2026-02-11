import streamlit as st
import time   # ⬅️ Used for simulating a delay in progress bar demo

# 1) Titles and Text

st.title("Title Example")        # Displays a big bold title
st.header("Header Example")         # Displays a section header
st.subheader("Subheader Example")   # Displays a smaller section header

# st.markdown lets you use Markdown formatting
# (*** makes bold+italic, *italic*, **bold**)
st.markdown("***Markdown Example:*** *italic* and **bold** text")

st.text("This is plain text.")      # Just plain text (no formatting)

# st.write is very flexible: can show strings, numbers, lists, dicts, DataFrames, etc.
st.write("st.write is flexible → can show text, numbers, dicts, DataFrames, etc.")

# st.code displays code nicely formatted (here with Python syntax highlighting)
st.code("print('Hello from code block')", language="python")

st.divider()  # Horizontal line for visual separation


# 2) User Input Widgets

name = st.text_input("Enter Your Name:")  # Text box input
st.write("Hello,", name)  # Shows typed name back

# Slider → user can pick a number between min=1 and max=100. Default = 20
age = st.slider("Pick Your Age:", 1, 100, 20)
st.write(f"You are {age} years old.")

# Selectbox → allows choosing ONE option only
hobbie = st.selectbox("Pick Your Hobbies:", ["Coding", "Gaming", "Music", "Sports"])
st.write("Your hobby:", hobbie)

# Multiselect → allows choosing MULTIPLE options
hobbies = st.multiselect("Pick Your Hobbies:", ["Coding", "Gaming", "Music", "Sports"])
st.write("Your hobbies: ", ', '.join(hobbies))

# Checkbox → returns True if checked, False otherwise
agree = st.checkbox("I agree to the terms and conditions")
if agree:
    st.success("✅ Thanks for agreeing!")  # Shown only if user agrees

# Radio buttons → allows picking ONE option, but displayed as buttons
gender = st.radio("Select Gender:", ["Male", "Female", "Other"])
st.write("Selected:", gender)

st.divider()


# 3) File Upload & Images

# st.file_uploader lets users upload files (here only .jpg or .png)
upload = st.file_uploader("Upload an Image", type=["jpg", "png"])

# If a file is uploaded, show it as an image
if upload is not None:
    st.image(upload, caption="Uploaded Image", use_container_width=True)

st.divider()


# 4) Buttons and Actions

# st.button returns True only when clicked
if st.button("Click Me!"):
    st.balloons()  # 🎈 Fun animation
    st.write("You clicked the button!")

st.divider()


# 5) Messages (colored alerts)

st.success("✅ Success message (Green)")   # Green box for success
st.error("❌ Error message (Red)")         # Red box for error
st.warning("⚠️ Warning message (Yellow)") # Yellow box for warning
st.info("ℹ️ Info message (Blue)")         # Blue box for info

st.divider()


# 6) Sidebar Navigation

# st.sidebar is used for navigation or filters
st.sidebar.title("Navigation Menu")

# Sidebar selectbox → dropdown in sidebar
option = st.sidebar.selectbox("Choose Section:", ["Home", "About", "Contact"])

if option == "Home":
    st.write("🏠 Welcome to the Home Section")
elif option == "About":
    st.write("ℹ️ This app is built with Streamlit.")
elif option == "Contact":
    st.write("📧 Contact us at: example@email.com")

st.divider()


# 7) Columns (Layout)

# st.columns(3) → divides screen into 3 equal-width columns
# col1, col2, col3 are "container variables" where we can place widgets/text
col1, col2, col3 = st.columns(3)

col1.write("This is column 1")  # Content for column 1
col2.write("This is column 2")  # Content for column 2
col3.write("This is column 3")  # Content for column 3

st.divider()


# 8) Expander (Hide/Show Info)

# st.expander creates collapsible content
with st.expander("See More Info"):
    st.write("This content is hidden until you expand it.")

st.divider()


# 9) Progress Bar & Status

st.write("Progress Example:")

# st.progress creates a progress bar, initialized at 0
progress = st.progress(0)

# Loop to update progress bar
for i in range(100):
    time.sleep(0.05)       # ⬅️ Adds delay so progress is visible (0.05 sec per loop)
    progress.progress(i+1) # ⬅️ Update bar to current progress (i+1 since i starts at 0)

st.success("🎉 Progress Completed!")  # Final success message