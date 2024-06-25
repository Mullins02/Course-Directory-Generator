# Course Directory Generator

This Python script automates the creation of directory structures for courses based on information provided in a formatted text file (`Course Directory Setup Doc.txt`).

## Features

- **Dynamic Folder Creation**: Automatically creates directories based on course-specific details such as assignments, labs, midterms, and defaults.
- **Input from Text File**: Reads course details from `Course Directory Setup Doc.txt`.
- **Default Directories**: Supports default directory structures specified in the text file.
- **Cross-platform**: Works on Windows, macOS, and Linux.

## Usage

1. **Setup**
   - Ensure Python 3.x is installed on your system.
   - Clone this repository: `git clone <repo_url>`.

2. **Running the Script**
   - Modify `Course Directory Setup Doc.txt` to specify course details.
   - Run the script: `python course_directory_generator.py`.

3. **Example Text File Format (`Course Directory Setup Doc.txt`)**

   ```plaintext   
   Defaults: .Syllabus, Notes, Lecture_Videos
   
   Course: ECE 2130 - Introduction to Circuits
   Assignments: 5
   Labs: 3
   Midterms: 2
