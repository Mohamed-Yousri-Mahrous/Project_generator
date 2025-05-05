import os
from cli import *


def create_project():

    while True:
        try:

            project_name = input("Enter project name: ").strip()

            if not (project_name and check_name(project_name)):
                print("\nProject name cannot be empty, Or already exists.")
                continue

            directories = [
                project_name,
                f"{project_name}/modules",
                f"{project_name}/tests",
                f"{project_name}/docs",
            ]

            files = {
                f"{project_name}/main.py": "# Main program entry point\n",
                f"{project_name}/config.py": "# Configuration settings and variables\n",
                f"{project_name}/requirements.txt": "# Project dependencies\n",
                f"{project_name}/README.md": f"# {project_name}\n\nProject description goes here.",
                f"{project_name}/modules/cli.py": "# Command Line Interface implementation\n",
                f"{project_name}/modules/__init__.py": "",
                f"{project_name}/tests/__init__.py": "",
                f"{project_name}/.gitignore": "__pycache__/\n*.pyc\n.env\n.venv/\nvenv/\n.idea/\n.vscode/\n",
            }

            for directory in directories:
                os.makedirs(directory, exist_ok=True)

            for file_path, content in files.items():
                with open(file_path, "w") as f:
                    f.write(content)

            print(f"\nProject '{project_name}' has been created successfully!")
            print("\nCreated structure:")
            print(f"├── {project_name}/")
            print("    ├── main.py")
            print("    ├── config.py")
            print("    ├── requirements.txt")
            print("    ├── README.md")
            print("    ├── modules/")
            print("    │   ├── __init__.py")
            print("    │   └── cli.py")
            print("    ├── tests/")
            print("    │   └── __init__.py")
            print("    └── docs/")

            git_status = (
                input("\nDo you want to initialize a git repository? (y/n): ")
                .strip()
                .lower()
            )
            if git_status == "y":
                os.system(f"cd {project_name} && git init")
                print("\nGit repository initialized.")

            create_border()
            pause()
            return
        except KeyboardInterrupt:
            print("\nOperation canceled by user.")
            return


if __name__ == "__main__":
    try:
        clear_screen()
        init_WorkingDirectory()
        create_project()
    except KeyboardInterrupt:
        print("\nOperation canceled by user.")
