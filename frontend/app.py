# frontend/app.py
import os
import flet as ft
import requests
from ui_components import TaskCard, LearningCard

API_BASE = os.getenv("API_BASE", "http://localhost:8000/api")

def show_error(page: ft.Page, msg: str):
    page.snack_bar = ft.SnackBar(ft.Text(msg))
    page.snack_bar.open = True
    page.update()

def main(page: ft.Page):
    page.title = "Daily Progress (Tasks & Learnings)"
    page.window_width = 420
    page.window_height = 720

    # Controls
    task_title = ft.TextField(label="Task title", expand=True)
    task_description = ft.TextField(label="Description", expand=True, multiline=True, max_lines=3)
    add_task_btn = ft.ElevatedButton("Add Task")
    load_tasks_btn = ft.ElevatedButton("Load Tasks")
    tasks_list = ft.ListView(expand=True, spacing=8, padding=10)

    learning_title = ft.TextField(label="Learning title", expand=True)
    learning_content = ft.TextField(label="Content", expand=True, multiline=True, max_lines=4)
    add_learning_btn = ft.ElevatedButton("Add Learning")
    load_learnings_btn = ft.ElevatedButton("Load Learnings")
    learnings_list = ft.ListView(expand=True, spacing=8, padding=10)

    def load_tasks(_=None):
        try:
            r = requests.get(f"{API_BASE}/tasks/", timeout=5)
            r.raise_for_status()
            tasks_list.controls.clear()
            for t in r.json():
                tasks_list.controls.append(TaskCard(t, reload_cb=load_tasks))
            page.update()
        except Exception as e:
            show_error(page, f"Could not load tasks: {e}")

    def add_task(_=None):
        data = {"title": task_title.value or "", "description": task_description.value or ""}
        if not data["title"].strip():
            show_error(page, "Task title required")
            return
        try:
            r = requests.post(f"{API_BASE}/tasks/", json=data, timeout=5)
            r.raise_for_status()
            task_title.value = ""
            task_description.value = ""
            load_tasks()
        except Exception as e:
            show_error(page, f"Could not add task: {e}")

    def load_learnings(_=None):
        try:
            r = requests.get(f"{API_BASE}/learnings/", timeout=5)
            r.raise_for_status()
            learnings_list.controls.clear()
            for l in r.json():
                learnings_list.controls.append(LearningCard(l))
            page.update()
        except Exception as e:
            show_error(page, f"Could not load learnings: {e}")

    def add_learning(_=None):
        data = {"title": learning_title.value or "", "content": learning_content.value or ""}
        if not data["title"].strip():
            show_error(page, "Learning title required")
            return
        try:
            r = requests.post(f"{API_BASE}/learnings/", json=data, timeout=5)
            r.raise_for_status()
            learning_title.value = ""
            learning_content.value = ""
            load_learnings()
        except Exception as e:
            show_error(page, f"Could not add learning: {e}")

    add_task_btn.on_click = add_task
    load_tasks_btn.on_click = load_tasks
    add_learning_btn.on_click = add_learning
    load_learnings_btn.on_click = load_learnings

    # Layout
    header = ft.Row([ft.Text("Daily Progress", size=24, weight=ft.FontWeight.BOLD)], alignment=ft.MainAxisAlignment.START)

    page.add(
        header,
        ft.Divider(height=1),
        ft.Text("Tasks", size=18, weight=ft.FontWeight.MEDIUM),
        ft.Row([task_title], alignment=ft.MainAxisAlignment.START, spacing=8),
        ft.Row([task_description], alignment=ft.MainAxisAlignment.START, spacing=8),
        ft.Row([add_task_btn, load_tasks_btn], spacing=12),
        tasks_list,
        ft.Divider(height=2),
        ft.Text("Learnings", size=18, weight=ft.FontWeight.MEDIUM),
        ft.Row([learning_title], alignment=ft.MainAxisAlignment.START),
        ft.Row([learning_content], alignment=ft.MainAxisAlignment.START),
        ft.Row([add_learning_btn, load_learnings_btn], spacing=12),
        learnings_list,
    )

    # initial load
    load_tasks()
    load_learnings()

if __name__ == "__main__":
    ft.app(target=main, view=ft.WEB_BROWSER)
