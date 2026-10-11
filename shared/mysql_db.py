"""Shared MySQL/MariaDB connection for USIRMS.

Default: 127.0.0.1:3306, user root, empty password, database usirms.
Override with environment variables or a repo-root .env (not committed).
"""

from __future__ import annotations

import os
from pathlib import Path

try:
    import pymysql
    from pymysql.cursors import DictCursor
    from pymysql.constants import CLIENT
except ImportError as exc:  # pragma: no cover
    raise SystemExit(
        "PyMySQL is required. From the repo root run:\n"
        "    python -m pip install PyMySQL"
    ) from exc

REPO = Path(__file__).resolve().parents[1]


def _load_dotenv() -> None:
    env_path = REPO / ".env"
    if not env_path.exists():
        return
    for raw in env_path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


_load_dotenv()

DB_NAME = os.environ.get("USIRMS_MYSQL_DATABASE", "usirms")


def server_settings() -> dict:
    return {
        "host": os.environ.get("USIRMS_MYSQL_HOST", "127.0.0.1"),
        "port": int(os.environ.get("USIRMS_MYSQL_PORT", "3306")),
        "user": os.environ.get("USIRMS_MYSQL_USER", "root"),
        "password": os.environ.get("USIRMS_MYSQL_PASSWORD", ""),
        "charset": "utf8mb4",
        "cursorclass": DictCursor,
        "autocommit": False,
        "client_flag": CLIENT.MULTI_STATEMENTS,
    }


class Connection:
    """Thin wrapper so scripts can use conn.execute(...) like sqlite3."""

    def __init__(self, raw: pymysql.connections.Connection):
        self.raw = raw
        self._cur = raw.cursor()

    def cursor(self):
        return self._cur

    def execute(self, sql: str, params=None):
        self._cur.execute(sql, params or ())
        return self._cur

    def executemany(self, sql: str, seq):
        self._cur.executemany(sql, seq)
        return self._cur

    def executescript(self, sql: str) -> None:
        self._cur.execute(sql)
        while self._cur.nextset():
            pass

    def commit(self) -> None:
        self.raw.commit()

    def rollback(self) -> None:
        self.raw.rollback()

    def close(self) -> None:
        try:
            self._cur.close()
        finally:
            self.raw.close()


def connect_server() -> Connection:
    return Connection(pymysql.connect(**server_settings()))


def connect(database: str | None = None) -> Connection:
    cfg = server_settings()
    cfg["database"] = database or DB_NAME
    return Connection(pymysql.connect(**cfg))


def ensure_database(name: str | None = None) -> None:
    db = name or DB_NAME
    conn = connect_server()
    try:
        conn.execute(
            f"CREATE DATABASE IF NOT EXISTS `{db}` "
            "CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci"
        )
        conn.commit()
    finally:
        conn.close()
