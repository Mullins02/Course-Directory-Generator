import os

# Creates folders depending on entered course information
def create_course_directory(course_name, course_assigns, course_labs, course_mids, course_defaults):
    base_dir = f"{course_name}"
    # Adds default 
    subdirectories = []
    for default in course_defaults:
        subdirectories.append(default)
    
    # Determines required folders
    if (course_labs > 0):
        if (course_labs > 1):
            subdirectories.append(f"Labs")
            for lab_num in range(1,course_labs):
                subdirectories.append(f"Labs/Lab {lab_num}")
        else:
            subdirectories.append(f"Lab")
    if (course_assigns > 0):
        if (course_assigns > 1):
            subdirectories.append(f"Assignments")
            for assign_num in range(1,course_assigns):
                subdirectories.append(f"Assignments/Assignment {assign_num}")
        else:
            subdirectories.append(f"Lab")
    if (course_mids > 0):
        if (course_mids > 1):
            subdirectories.append(f"Midterms")
            for mid_num in range(1,course_mids):
                subdirectories.append(f"Midterms/Midterm {mid_num}")
        else:
            subdirectories.append(f"Midterm")
    
    # Begins creating course folders
    print(f'Creating directory for {course_name}')
    for subdirectory in subdirectories:
        full_path = os.path.join(base_dir, subdirectory)
        path = full_path.split('\\')[-1]
        path = path.split('/')[-1]
        if not os.path.exists(full_path):
            os.makedirs(full_path, exist_ok=True)
            print(f"\tCreated directory: '{path}'")
        else:
            print(f"\tDirectory '{path}' already exists. Skipping creation.")

    print(f"Directory for course {course_name} completed.\n")

# Reads information from the text doc
def read_course_info(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    courses = []
    course_info = {}
    for line in lines:
        line = line.strip()
        if line.startswith("Defaults:"):
            if course_info:
                courses.append(course_info)
                course_info = {}                
            course_info['defaults'] = []
            defaults_line = line.split(':')[1].strip()
            if defaults_line:
                defaults = defaults_line.split(',')
                for default in defaults:
                    course_info['defaults'].append(default.strip())
        elif line.startswith("Course:"):
            course_info['course_name'] = line.split(':')[1].strip()
        elif line.startswith("Assignments:"):
            course_info['assignments'] = int(line.split(':')[1].strip())
        elif line.startswith("Labs:"):
            course_info['labs'] = int(line.split(':')[1].strip())
        elif line.startswith("Midterms:"):
            course_info['midterms'] = int(line.split(':')[1].strip())

    if course_info:
        courses.append(course_info)

    return courses


if __name__ == "__main__":
    file_path = 'Course Directory Setup Doc.txt'
    courses = read_course_info(file_path)

    for course in courses:
        course_name = course.get('course_name')
        course_labs = course.get('labs', 0)
        course_assigns = course.get('assignments', 0)
        course_mids = course.get('midterms', 0)
        course_defaults = course.get('defaults', 0)

        create_course_directory(course_name, course_assigns, course_labs, course_mids, course_defaults)
