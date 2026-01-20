# PostgreSQL Installation Guide for Windows

Since you are teaching this class, you **must** have PostgreSQL installed to demonstrate the connection.

## 1. Download the Installer
*   Go to the official download page: [EnterpriseDB PostgreSQL Installer](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads).
*   Download the version corresponding to your Django support (PostgreSQL 15 or 16 is recommended for modern Django).

## 2. Installation Steps
1.  **Run the Installer**: Double-click the downloaded `.exe` file.
2.  **Select Components**: Ensure **PostgreSQL Server**, **pgAdmin 4**, and **Command Line Tools** are checked.
3.  **Data Directory**: Keep the default or pick a location with space.
4.  **Password**: **IMPORTANT**. You will be asked to set a password for the "superuser" (default username is `postgres`).
    *   *Tip for Class*: Set it to something simple like `admin` or `root` for the demo, but warn students to use strong passwords in production.
    *   **Write this password down!** You will need it for your `.env` file (`DB_PASSWORD`).
5.  **Port**: Keep the default `5432`.
6.  **Locale**: Default is usually fine.
7.  **Finish**: Launch Stack Builder? You can uncheck this; you usually don't need extra add-ons for a basic class.

## 3. Verify Installation
1.  Open the **Windows Start Menu** and search for **pgAdmin 4**. Open it.
2.  It will ask for a master password (for pgAdmin itself) or the database password you just set.
3.  Once open, click on "Servers" > "PostgreSQL X".
4.  If it connects, you are ready!

## 4. Class Demo Tip
During the class, users often struggle with the "PATH" environment variable.
*   The installer usually handles this, but if running `psql` in the terminal fails, just use **pgAdmin** to create the database graphically. It's often easier for beginners.
