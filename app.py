import streamlit as st
import json
import os


FILE_NAME = "tasks.json"


# -----------------------------
# Load tasks
# -----------------------------
def load_tasks():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


# -----------------------------
# Save tasks
# -----------------------------
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# -----------------------------
# Add task
# -----------------------------
def add_task(task_name):
    tasks = load_tasks()

    task = {
        "name": task_name,
        "status": "Pending"
    }

    tasks.append(task)
    save_tasks(tasks)


# -----------------------------
# Complete task
# -----------------------------
def complete_task(index):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks[index]["status"] = "Completed"
        save_tasks(tasks)


# -----------------------------
# Update task
# -----------------------------
def update_task(index, new_name):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks[index]["name"] = new_name
        save_tasks(tasks)


# -----------------------------
# Delete task
# -----------------------------
def delete_task(index):
    tasks = load_tasks()

    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)


# -----------------------------
# Clear completed tasks
# -----------------------------
def clear_completed():
    tasks = load_tasks()

    tasks = [
        task for task in tasks
        if task["status"] != "Completed"
    ]

    save_tasks(tasks)


# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="To-Do List Manager",
    page_icon="✅",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------
st.title("✅ To-Do List Manager")
st.write("A simple Python-based task management application.")


# -----------------------------
# Load tasks
# -----------------------------
tasks = load_tasks()


# -----------------------------
# Statistics
# -----------------------------
total_tasks = len(tasks)

completed_tasks = sum(
    1 for task in tasks
    if task["status"] == "Completed"
)

pending_tasks = total_tasks - completed_tasks


col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total", total_tasks)

with col2:
    st.metric("Completed", completed_tasks)

with col3:
    st.metric("Pending", pending_tasks)


st.divider()


# -----------------------------
# Add Task
# -----------------------------
st.subheader("➕ Add Task")

new_task = st.text_input("Enter a new task")

if st.button("Add Task"):

    if new_task.strip():

        add_task(new_task.strip())

        st.success("Task added successfully!")

        st.rerun()

    else:

        st.warning("Please enter a task.")


st.divider()


# -----------------------------
# Display Tasks
# -----------------------------
st.subheader("📋 Your Tasks")

tasks = load_tasks()

if len(tasks) == 0:

    st.info("No tasks available. Add your first task!")

else:

    for index, task in enumerate(tasks):

        col1, col2, col3, col4 = st.columns(
            [4, 2, 1, 1]
        )

        with col1:

            if task["status"] == "Completed":
                st.markdown(
                    f"~~{task['name']}~~"
                )
            else:
                st.write(task["name"])

        with col2:
            st.write(task["status"])

        with col3:

            if task["status"] == "Pending":

                if st.button(
                    "✓",
                    key=f"complete_{index}"
                ):

                    complete_task(index)
                    st.rerun()

        with col4:

            if st.button(
                "🗑️",
                key=f"delete_{index}"
            ):

                delete_task(index)
                st.rerun()


st.divider()


# -----------------------------
# Update Task
# -----------------------------
st.subheader("✏️ Update Task")

tasks = load_tasks()

if tasks:

    task_names = [
        task["name"]
        for task in tasks
    ]

    selected_task = st.selectbox(
        "Select a task",
        task_names
    )

    new_name = st.text_input(
        "Enter new task name"
    )

    if st.button("Update Task"):

        selected_index = task_names.index(
            selected_task
        )

        if new_name.strip():

            update_task(
                selected_index,
                new_name.strip()
            )

            st.success(
                "Task updated successfully!"
            )

            st.rerun()

        else:

            st.warning(
                "Task name cannot be empty."
            )


st.divider()


# -----------------------------
# Clear completed tasks
# -----------------------------
if st.button("🧹 Clear Completed Tasks"):

    clear_completed()

    st.success(
        "Completed tasks cleared!"
    )

    st.rerun()