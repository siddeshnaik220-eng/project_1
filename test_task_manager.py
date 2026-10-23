"""Tests for academic task creation, persistence, updates, and deletion."""

import json
import tempfile
import unittest
from pathlib import Path

from task_manager import TaskManager


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()
        self.storage_path = Path(self.temp_directory.name) / "tasks.json"
        self.manager = TaskManager(self.storage_path)

    def tearDown(self):
        self.temp_directory.cleanup()

    def create_task(self):
        return self.manager.create_task(
            "Essay", "Write the history essay", "2026-11-15", "High"
        )

    def test_create_and_reload_task(self):
        created = self.create_task()

        loaded = TaskManager(self.storage_path).list_tasks()

        self.assertEqual(len(loaded), 1)
        self.assertEqual(loaded[0], created)
        self.assertFalse(loaded[0].completed)

    def test_update_task_fields_and_completion(self):
        created = self.create_task()

        updated = self.manager.update_task(
            created.task_id,
            title="Revised essay",
            description="Add citations",
            due_date="2026-11-20",
            priority="Medium",
            completed=True,
        )

        self.assertEqual(updated.title, "Revised essay")
        self.assertEqual(updated.description, "Add citations")
        self.assertEqual(updated.due_date, "2026-11-20")
        self.assertEqual(updated.priority, "Medium")
        self.assertTrue(updated.completed)
        self.assertEqual(TaskManager(self.storage_path).list_tasks()[0], updated)

    def test_update_only_changes_requested_fields(self):
        created = self.create_task()

        updated = self.manager.update_task(created.task_id, completed=True)

        self.assertEqual(updated.title, created.title)
        self.assertEqual(updated.priority, created.priority)
        self.assertTrue(updated.completed)

    def test_delete_task(self):
        created = self.create_task()

        deleted = self.manager.delete_task(created.task_id)

        self.assertEqual(deleted, created)
        self.assertEqual(self.manager.list_tasks(), [])
        self.assertEqual(TaskManager(self.storage_path).list_tasks(), [])

    def test_invalid_task_data_is_rejected(self):
        invalid_tasks = (
            ("  ", "Description", "2026-11-15", "High"),
            ("Essay", "Description", "not-a-date", "High"),
            ("Essay", "Description", "20261115", "High"),
            ("Essay", "Description", "2026-11-15", "Urgent"),
        )
        for task_data in invalid_tasks:
            with self.subTest(task_data=task_data):
                with self.assertRaises(ValueError):
                    self.manager.create_task(*task_data)

    def test_missing_task_raises_key_error(self):
        with self.assertRaises(KeyError):
            self.manager.delete_task("missing")

    def test_malformed_persisted_data_is_reported(self):
        self.storage_path.write_text(json.dumps({"not": "a list"}), encoding="utf-8")

        with self.assertRaisesRegex(ValueError, "JSON list"):
            TaskManager(self.storage_path)


if __name__ == "__main__":
    unittest.main()
