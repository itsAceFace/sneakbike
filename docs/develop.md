# Developer Resources

For development operations, see the [Devops Docs](./devops.md).

- [Developer Resources](#developer-resources)
  - [Development Practices](#development-practices)
  - [Misc Scripts](#misc-scripts)

---

---

## Development Practices

Most scripts will be written in Python 3.6+ with standard Black formatting. For bash scripts, value readability over being concise.

---

---

## Misc Scripts

We have collected a few helpful scripts at `/scripts`. **All Python files are Py3.6+**. Below are descriptions of each file:

- `bounding_box_creator.py` creates a "bounding box" (a frame around a window) of any size, color, thickness, etc. See example at the bottom of the file to run it.
  - Requires PIL but Anaconda install should suffice.
