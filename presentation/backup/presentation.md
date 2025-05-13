class: center, middle, inverse

# Backups for Software Engineers

---

# Why Backups Matter

**"There are two types of people: those who backup, and those who will."**

- Prevent data loss from hardware failure, human error, or malware
- Essential for both personal and professional work
- Critical part of any software development workflow

---

# Backup Basics

**3-2-1 Rule:**
- 3 copies of your data
- 2 different media types
- 1 copy offsite

**Common Backup Types:**
- Full backup
- Incremental backup
- Differential backup

---

# Basic Backup Commands

```bash
# Copy files (basic backup)
cp important_file.txt important_file_backup.txt

# Archive directory
tar -czvf project_backup.tar.gz /path/to/project

# Sync directories (like incremental backup)
rsync -av --delete /source/folder /backup/folder
```

---

# The `tar` Command Explained

**Tape Archive** - Bundles files into a single archive file

Basic syntax:

```bash
tar [options] [archive_name] [files_to_archive]
```

### Common options:

-c: Create new archive
-x: Extract files
-v: Verbose output
-f: Specify filename
-z: Compress with gzip
-j: Compress with bzip2

### Examples:

```bash
# Create compressed archive
tar -czvf backup.tar.gz /path/to/files

# Extract archive
tar -xzvf backup.tar.gz

# List contents without extracting
tar -tzvf backup.tar.gz
```
---

# The rsync Command Explained

Remote Sync - Efficient file copying/synchronization

### Key features:

- Only copies changed files (incremental)
- Preserves permissions/timestamps
- Can work over network
- Supports compression

### Basic syntax:

```bash
rsync [options] source destination
```

### Common options:

-a: Archive mode (recursive + preserve attributes)
-v: Verbose output
-z: Compress during transfer
--delete: Remove files in dest not in source
--exclude: Skip specified files

### Examples:

```bash
# Local directory sync
rsync -av /source/ /backup/

# Remote backup
rsync -avz -e ssh /local/path user@remote:/backup/path

# Dry run (test first!)
rsync -avn /source/ /backup/
```

---

# Automating Backups with Bash

Create a backup script (backup.sh):

```bash
#!/bin/bash
BACKUP_DIR="/home/user/backups"
PROJECT_DIR="/home/user/projects"

# Create timestamped backup
tar -czvf "$BACKUP_DIR/project_$(date +%Y%m%d).tar.gz" "$PROJECT_DIR"

# Keep only last 7 backups
ls -t "$BACKUP_DIR"/*.tar.gz | tail -n +8 | xargs rm -f
```

Make it executable: `chmod +x backup.sh`

---

# The crontab System Explained
Cron - Time-based job scheduler

### Basic structure:

```
* * * * * command_to_execute
┬ ┬ ┬ ┬ ┬
│ │ │ │ └─ Day of week (0-6) (Sunday=0)
│ │ │ └─── Month (1-12)
│ │ └───── Day of month (1-31)
│ └─────── Hour (0-23)
└───────── Minute (0-59)
```

### Special characters:

*: Any value
,: Value list separator
-: Range of values
/: Step values

### Examples:

```bash
# Edit crontab
crontab -e

# Run backup daily at 3am
0 3 * * * /path/to/backup.sh

# Run every Monday at 5pm
0 17 * * 1 /path/weekly_task.sh

# Run every 15 minutes
*/15 * * * * /path/check_status.sh
```

---

# Scheduling Backups with Cron

Edit crontab: crontab -e

Add line to run daily at 2am:

```bash
0 2 * * * /path/to/backup.sh
```

Verify it's scheduled:

```bash
crontab -l
```

---

# Cloud Backup Options

Cloud Provider (Azure, Google Cloud, Amazon, etc), Google Drive, Dropbox, GitHub (for code)

---

# Version Control as Backup
Git provides file history and remote backup:

```bash
# Initialize repo
git init

# Add files
git add .

# Commit changes
git commit -m "Project backup"

# Push to remote
git remote add origin https://github.com/user/repo.git
git push -u origin main
```

---

# Backup Verification

Always verify your backups!

```bash
# Check file contents
tar -tzvf backup.tar.gz | head

# Test restore
mkdir test_restore && tar -xzvf backup.tar.gz -C test_restore

# Compare checksums
md5sum original.txt backup.txt
```

---

# Hands-On Practice

1. Create a backup script for your home directory

2. Schedule it to run weekly

3. Set up a Git repository for your code

4. Test restoring from a backup

**Remember**: A backup isn't complete until you've tested restoring it!

