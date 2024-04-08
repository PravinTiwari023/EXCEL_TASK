import streamlit as st

# Function to save submissions to a file or database
def save_submission(user_name, task_solution):
    # This is a placeholder function.
    # You can implement saving to a file, database, or any other storage here.
    with open("submissions.txt", "a") as file:
        file.write(f"User: {user_name}, Solution: {task_solution}\n")

# Streamlit UI elements
st.title('Task Submission Portal')
st.subheader(':orange[Upload your file in google drive and copy the link of file and share.]')
user_name = st.text_input('Drive link')
task_solution = st.text_area('How was the task overall!!')

if st.button('Submit'):
    if user_name and task_solution:
        save_submission(user_name, task_solution)
        st.success('Thanks for completing the task!')
    else:
        st.error('Please fill in all fields.')