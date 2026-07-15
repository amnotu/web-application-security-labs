# Lab 01: Foundations

## Objective

Review the basic technologies used throughout the web application security labs: shared folders, SQL databases, HTML, JavaScript, and the Document Object Model.

This lab documents the foundation work needed before later web application security testing.

## Methodology Phase

PTES Phase: Pre-engagement / Technical Preparation

This lab prepares the local working environment and reviews application technologies that later vulnerability testing depends on.

## Scope

Testing and setup were performed only inside the local VMware lab.

Included systems:

- Kali Linux tester VM
- Local MariaDB service
- Local HTML/JavaScript demo file
- Local lab files from the VMware shared folder

No public systems were tested.

## Part 1: Shared Folder Check

The VMware shared folder was confirmed in Lab 00. It is used to move course files and lab evidence between the Windows host and Kali.

Mounted path:

`/mntt/hgfs/File to share with kali Labs`

Files observed:

- `Auth.zip`
- `create.zip`
- `hashes.tar`
- `salted.tar`

## Part 2: SQL Database Setup

The SQL setup used `create.zip` from the shared folder. The archive was copied into the Lab 01 evidence folder and extracted to obtain `create.sql`.

The local database service was MariaDB.

Observed version:

`11.8.8-MariaDB-1 from Debian`

The SQL script created a database named:

`pencourse`

## Tables Created

| Table | Row Count |
|---|---:|
| `customer` | 20 |
| `product` | 39 |
| `order` | 20 |
| `item` | 43 |

## Part 3: SQL Schema Review

The schema review confirmed four tables:

- `customer`
- `product`
- `order`
- `item`

The `customer` table contains personal-style sample data and password hashes. For that reason, the public evidence avoids showing raw customer records, emails, phone numbers, addresses, or password hashes.

## Part 4: SQL Query Practice

The following SQL concepts were practiced using sanitized output:

- Basic `SELECT`
- `WHERE` filtering
- `ORDER BY`
- `GROUP BY`
- Aggregate functions with `COUNT()` and `AVG()`
- `JOIN`
- `UPDATE` inside a transaction
- `ROLLBACK`
- `DELETE` using a temporary table

The query evidence avoids personal-style customer records and focuses on product data, table counts, grouped values, and transaction behavior.

## Part 5: HTML, JavaScript, and DOM Review

A small local page was created to review how HTML, JavaScript, and the DOM work together.

Local file:

`labs/01-foundations/html-js-dom/foundations-demo.html`

The page contains:

- HTML structure
- A heading
- A paragraph
- An input field
- A button
- An output paragraph
- JavaScript that reacts to a button click
- DOM updates using `getElementById()` and `textContent`

## Key Results

| Check | Result |
|---|---|
| Database loaded | `pencourse` exists |
| Tables verified | `customer`, `product`, `order`, `item` |
| Customer rows | 20 |
| Product rows | 39 |
| Order rows | 20 |
| Item rows | 43 |
| Country aggregate | Norway = 20 |
| Update test | Stock changed from 120 to 119 inside transaction |
| Rollback test | Stock returned to 120 |
| Delete test | Temporary row deleted from temporary table only |
| HTML test | Local page loaded in Firefox |
| JavaScript test | Button click read input value |
| DOM test | Page text changed after JavaScript event |

## Commands and Files Used

Check database version:

`sudo mysql -u root -e "SELECT VERSION();"`

Reset the database before loading:

`sudo mysql -u root -e "DROP DATABASE IF EXISTS pencourse;"`

Load the SQL script:

`sudo mysql -u root < create.sql`

Verify the database:

`sudo mysql -u root -e "SHOW DATABASES LIKE 'pencourse';"`

Verify tables:

`sudo mysql -u root -e "USE pencourse; SHOW TABLES;"`

Open the HTML/JavaScript/DOM demo:
````bash
firefox labs/01-foundations/html-js-dom/foundations-demo.html
````
## Evidence

| Evidence | What it shows |
|---|---|
| [`sql-database-setup-verification.txt`](evidence/sql-database-setup-verification.txt) | MariaDB version, database check, table list, and row counts. |
| [`sql-schema-review.txt`](evidence/sql-schema-review.txt) | Table names and column structure. |
| [`sql-query-practice.txt`](evidence/sql-query-practice.txt) | Full sanitized SQL query-practice output. |
| [`sql-query-practice-summary.txt`](evidence/sql-query-practice-summary.txt) | Short summary suitable for screenshot evidence. |
| [`html-js-dom-summary.txt`](evidence/html-js-dom-summary.txt) | Summary of the local HTML, JavaScript, and DOM test. |
| [`foundations-demo.html`](html-js-dom/foundations-demo.html) | Local demo page used for HTML, JavaScript, and DOM review. |
| [`01-sql-database-loaded-and-tables-verified.png`](../../assets/screenshots/01-foundations/01-sql-database-loaded-and-tables-verified.png) | Screenshot showing the database was loaded and verified. |
| `02-sql-query-practice-summary.png` | Screenshot showing the SQL query-practice summary. |
| `03-html-js-dom-local-demo.png` | Screenshot showing the local page after JavaScript changed the DOM. |
| `04-html-js-dom-summary.png` | Screenshot showing the HTML, JavaScript, and DOM summary. |

Screenshot locations:

`assets/screenshots/01-foundations/01-sql-database-loaded-and-tables-verified.png`

`assets/screenshots/01-foundations/02-sql-query-practice-summary.png`

`assets/screenshots/01-foundations/03-html-js-dom-local-demo.png`

`assets/screenshots/01-foundations/04-html-js-dom-summary.png`

Text evidence locations:

`labs/01-foundations/evidence/sql-database-setup-verification.txt`

`labs/01-foundations/evidence/sql-schema-review.txt`

`labs/01-foundations/evidence/sql-query-practice.txt`

`labs/01-foundations/evidence/sql-query-practice-summary.txt`

`labs/01-foundations/evidence/html-js-dom-summary.txt`

## Observations

The `pencourse` database was created successfully. The expected tables are present, and row counts confirm that the sample data was loaded.

The SQL query-practice section confirmed that the database can be queried, filtered, grouped, joined, updated inside a transaction, rolled back, and tested with a temporary delete operation.

The HTML, JavaScript, and DOM section confirmed that JavaScript can read an input value, respond to a click event, and modify visible page content through the DOM.

Raw course files are not included in the public repository. The repository `.gitignore` excludes `create.zip` and `create.sql`.

## Result

Lab 01 foundations work is complete.

## Security Notes

This lab uses local training data only. Raw SQL files, sample personal-style records, and password hashes are not included in the public repository.
