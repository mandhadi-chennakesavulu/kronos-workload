import streamlit as st
import time

# Initialize session state variables
if 'notepad' not in st.session_state:
    st.session_state['notepad'] = [""]  # A list of pages
if 'running' not in st.session_state:
    st.session_state['running'] = False  # Controls the repetition process
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 0  # Current page index

# Function to repeat input
def repeat_input():
    while st.session_state['running']:
        # Check the word count on the current page
        word_count = len(st.session_state['notepad'][st.session_state['current_page']].split())
        
        # If word count exceeds 1000, switch to the next page
        if word_count >= 1000:
            # Add a new page if needed
            if len(st.session_state['notepad']) <= st.session_state['current_page'] + 1:
                st.session_state['notepad'].append("")
            st.session_state['current_page'] += 1
        
        # Add input text to the current notepad page
        st.session_state['notepad'][st.session_state['current_page']] += st.session_state['input_text'] + "\n"
        
        # Use st.empty() to create a placeholder for the notepad content
        with st.empty():
            st.text_area(f"Notepad - Page {st.session_state['current_page'] + 1}",
                         st.session_state['notepad'][st.session_state['current_page']], height=400)
        
        time.sleep(1)  # 1-second delay between repetitions

# Function to start the repetition
def start_repeating():
    if not st.session_state['running']:
        st.session_state['running'] = True
        repeat_input()  # Start repeating

# Function to stop the repetition
def stop_repeating():
    st.session_state['running'] = False

# Function to add a new page
def add_new_page():
    st.session_state['notepad'].append("")
    st.session_state['current_page'] = len(st.session_state['notepad']) - 1

# Function to switch to a different page
def switch_page(page_index):
    st.session_state['current_page'] = page_index

# Streamlit UI components
st.title("Automated Kronos Simulation App with Pages")

# Input field
st.session_state['input_text'] = st.text_input("Enter the text to be repeated in the notepad:")

# Start and Stop buttons
if st.button("Start"):
    start_repeating()

if st.button("Stop"):
    stop_repeating()

if st.button("Add New Page"):
    add_new_page()

# Display the current page of the notepad
st.text_area(f"Notepad - Page {st.session_state['current_page'] + 1}",
             st.session_state['notepad'][st.session_state['current_page']], height=400)

# Page navigation buttons
if len(st.session_state['notepad']) > 1:
    cols = st.columns(len(st.session_state['notepad']))
    for i, col in enumerate(cols):
        with col:
            if st.button(f"Page {i + 1}", key=f"page_{i}"):
                switch_page(i)
