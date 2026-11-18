import sqlite3
import unittest
from main import audit_connection

class SqliteAuditTests(unittest.TestCase):
    def test_detects_orphaned_foreign_key(self):
        db = sqlite3.connect(":memory:")
        db.execute("CREATE TABLE parent(id INTEGER PRIMARY KEY)")
        db.execute("CREATE TABLE child(parent_id INTEGER REFERENCES parent(id))")
        db.execute("INSERT INTO child(parent_id) VALUES (42)")
        report = audit_connection(db)
        self.assertEqual(len(report["foreign_key_violations"]), 1)
        self.assertFalse(report["ok"])
    def test_clean_database(self):
        db = sqlite3.connect(":memory:")
        db.execute("CREATE TABLE item(id INTEGER PRIMARY KEY)")
        self.assertTrue(audit_connection(db)["ok"])

if __name__ == "__main__":
    unittest.main()
