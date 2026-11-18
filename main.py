#!/usr/bin/env python3
"""Audit SQLite foreign-key and structural integrity without writing to the DB."""
import argparse
import json
import sqlite3
import sys
from pathlib import Path

def audit_connection(connection):
    violations = connection.execute("PRAGMA foreign_key_check").fetchall()
    integrity = [row[0] for row in connection.execute("PRAGMA integrity_check").fetchall()]
    tables = [row[0] for row in connection.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
    )]
    return {
        "tables": tables,
        "foreign_key_violations": [
            {"table": row[0], "rowid": row[1], "parent": row[2], "constraint": row[3]}
            for row in violations
        ],
        "integrity": integrity,
        "ok": not violations and integrity == ["ok"]
    }

def audit_path(path):
    db_path = Path(path).expanduser().resolve()
    if not db_path.is_file():
        raise FileNotFoundError(db_path)
    uri = db_path.as_uri() + "?mode=ro"
    connection = sqlite3.connect(uri, uri=True)
    try:
        return audit_connection(connection)
    finally:
        connection.close()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("database")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    try:
        report = audit_path(args.database)
    except (OSError, sqlite3.Error) as exc:
        print(f"sqlite-fk-audit: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Tables: {len(report['tables'])}")
        print(f"Foreign-key violations: {len(report['foreign_key_violations'])}")
        for item in report["foreign_key_violations"]:
            print(f"- {item['table']} row {item['rowid']} -> {item['parent']} (constraint {item['constraint']})")
        print("Integrity: " + "; ".join(report["integrity"]))
    return 0 if report["ok"] else 1

if __name__ == "__main__":
    raise SystemExit(main())
