# File Integrity Monitor

A Python-based File Integrity Monitoring (FIM) project designed to detect unauthorized or unexpected changes to files by comparing their SHA-256 hashes.

> **Status:** In development  
> This repository documents the project and its development roadmap. Features will be marked as implemented as they are completed and tested.

## Overview

File Integrity Monitoring (FIM) is a security practice used to identify changes to important files. By calculating and comparing cryptographic hashes, a monitoring tool can help detect when files have been modified, added, or deleted.

The goal of this project is to build a command-line tool that monitors a directory and reports changes in its files.

## Planned Features

- [ ] Scan files inside a selected directory.
- [ ] Calculate SHA-256 hashes using Python's `hashlib`.
- [ ] Store baseline file information.
- [ ] Compare current hashes against the stored baseline.
- [ ] Detect modified files.
- [ ] Detect newly created files.
- [ ] Detect deleted files.
- [ ] Display a clear report of detected changes.
- [ ] Add automated tests.

## Technologies

- **Python** — main programming language.
- **hashlib** — cryptographic hash calculation.
- **pathlib** — filesystem and path handling.
- **JSON or SQLite** — planned storage for baseline data.
- **pytest** — planned automated testing.

## How It Works

The planned monitoring workflow is:

1. Select a directory to monitor.
2. Discover the files inside that directory.
3. Read each file and calculate its SHA-256 hash.
4. Save the initial results as a baseline.
5. Scan the directory again later.
6. Compare the new results with the baseline.
7. Report files that were modified, added, or deleted.

## Example of Expected Output

The following is an illustrative example of the report the tool aims to produce:

```text
[FILE MODIFIED] config.txt
[FILE ADDED] new_file.txt
[FILE DELETED] old_file.txt

Scan completed.
```

This output is an example of the planned behavior, not a claim that the feature is already implemented.

## Project Structure

The project structure will be documented here as the implementation evolves.

## Learning Objectives

This project is being developed to practice:

- File handling in Python.
- Cryptographic hashing and SHA-256.
- Filesystem navigation.
- Data persistence.
- Change detection.
- Basic security monitoring concepts.
- Testing and clean code practices.

## Roadmap

- [ ] **Phase 1:** Build the SHA-256 hashing function.
- [ ] **Phase 2:** Scan directories and collect file metadata.
- [ ] **Phase 3:** Save and load a baseline.
- [ ] **Phase 4:** Detect modified, added, and deleted files.
- [ ] **Phase 5:** Generate readable security reports.
- [ ] **Phase 6:** Add tests and improve reliability.

## Security Notes

SHA-256 hashes can help identify changes to file contents, but a hash alone does not prove that a file is trustworthy. The baseline must also be protected: if an attacker can modify both a monitored file and its stored baseline, they may hide unauthorized changes.

This project is intended for educational and defensive security purposes.

## Author

**William Gabriel Roque de Assis**

- GitHub: [@william-grassis67](https://github.com/william-grassis67)

---

*This project is part of my learning journey in Python programming and cybersecurity.*
