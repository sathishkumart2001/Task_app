# frontend/ui_components.py
import flet as ft
import requests
import os

API_BASE = os.getenv("API_BASE", "http://localhost:8000/api")

class TaskCard(ft.Card):
    def __init__(self, task: dict, reload_cb=None):
        self.task = task
        self.reload_cb = reload_cb
        completed = task.get("completed", False)
        title = task.get("title", "(no title)")
        description = task.get("description", "")
        assigned_to = task.get("assigned_to", "")
        super().__init__(
            content=ft.Container(
                ft.Column(
                    [
                        ft.Row(
                            [
                                ft.Checkbox(value=completed, on_change=self._toggle_completed),
                                ft.Text(title, weight=ft.FontWeight.BOLD),
                                ft.IconButton(ft.icons.DELETE, on_click=self._delete, tooltip="Delete"),
                            ],
                            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                        ),
                        ft.Text(description or ""),
                        ft.Text(f"Assigned to: {assigned_to}" if assigned_to else ""),
                    ],
                    tight=True,
                ),
                padding=10,
            ),
            elevation=1,
        )

    def _toggle_completed(self, e):
        try:
            new_val = e.control.value
            requests.patch(f"{API_BASE}/tasks/{self.task['_id']}", json={"completed": new_val}, timeout=5)
            if self.reload_cb:
                self.reload_cb()
        except Exception as exc:
            print("Error toggling completed:", exc)

    def _delete(self, e):
        try:
            requests.delete(f"{API_BASE}/tasks/{self.task['_id']}", timeout=5)
            if self.reload_cb:
                self.reload_cb()
        except Exception as exc:
            print("Error deleting task:", exc)

class LearningCard(ft.Card):
    def __init__(self, learning: dict):
        title = learning.get("title", "(no title)")
        content = learning.get("content", "")
        super().__init__(
            content=ft.Container(
                ft.Column([ft.Text(title, weight=ft.FontWeight.BOLD), ft.Text(content or "")]),
                padding=10,
            ),
            elevation=0.5,
        )
