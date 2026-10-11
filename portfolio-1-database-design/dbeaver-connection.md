# Open USIRMS in DBeaver

The relational system of record is **MySQL/MariaDB** (InnoDB), database name `usirms`. DBeaver is already installed on this machine.

## Connection settings

| Field | Value |
| --- | --- |
| Driver | **MariaDB** (or MySQL if you installed Oracle MySQL) |
| Host | `127.0.0.1` |
| Port | `3306` |
| Database | `usirms` |
| User | `root` |
| Password | empty unless you set `USIRMS_MYSQL_PASSWORD` |

Optional extra schemas after Portfolio 5: `usirms_frag_main`, `usirms_frag_north`, `usirms_replica`.

## First-time steps

1. Start the MariaDB/MySQL Windows service if it is not running.
2. From the repo root:
   ```text
   python -m pip install PyMySQL
   python portfolio-1-database-design/scripts/build_database.py --scale full
   ```
3. In DBeaver: **Database → New Database Connection → MariaDB**.
4. Fill the table above → **Test Connection** → **Finish**.
5. Expand `usirms` → **Tables** / **Views**.

## If login fails

Create a repo-root `.env` (gitignored):

```text
USIRMS_MYSQL_HOST=127.0.0.1
USIRMS_MYSQL_PORT=3306
USIRMS_MYSQL_USER=root
USIRMS_MYSQL_PASSWORD=your-password
USIRMS_MYSQL_DATABASE=usirms
```

Then rebuild. Do not commit `.env`.
