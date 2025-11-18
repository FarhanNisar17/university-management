import PyPDF2
import os
from pathlib import Path
import sys

# Ensure project root is on sys.path so imports like `util` and `models` resolve
PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from util.database import create_app
from util.extensions import db
from models.thirdsem import ThirdSemStudent
from util.database import setup_database

app = create_app()
app.app_context().push()
# Ensure DB tables exist
setup_database(app)

# Expect `students.pdf` in the project root (one level up from this script)
project_root = Path(__file__).resolve().parents[1]
# Accept either project_root/students.pdf or project_root/students.pdf/students.pdf
file_candidate = project_root / 'students.pdf'
nested_candidate = project_root / 'students.pdf' / 'students.pdf'
pdf_path = None
# Prefer a direct file if present
if file_candidate.is_file():
    pdf_path = file_candidate
elif nested_candidate.is_file():
    pdf_path = nested_candidate

if pdf_path is None:
    print(f"PDF not found. Checked: {file_candidate} and {nested_candidate}")
    raise SystemExit(1)

reader = PyPDF2.PdfReader(str(pdf_path))
text = ""

for page in reader.pages:
    page_text = page.extract_text() or ""
    text += page_text + "\n"

lines = [ln.strip() for ln in text.splitlines() if ln.strip()]

# Very simple parsing: adjust according to your PDF's structure
for line in lines:
    # Skip header-like lines
    if line.lower().startswith('name') or line.lower().startswith('roll'):
        continue

    parts = line.split()
    if len(parts) < 2:
        continue

    # Assume roll number is the second token
    name = parts[0]
    roll = parts[1]
    department = ' '.join(parts[2:]) if len(parts) > 2 else None

    student = ThirdSemStudent(name=name, roll=roll, department=department)
    db.session.add(student)

db.session.commit()

print("PDF Data Imported Successfully")
