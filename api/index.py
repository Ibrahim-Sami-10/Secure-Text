import os
import sys

# Ensure the root directory is on the Python path so app can be imported
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app

# Vercel WSGI entrypoint
app = app
