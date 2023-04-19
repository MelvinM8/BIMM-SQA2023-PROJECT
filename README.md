# BIMM-SQA2023-PROJECT
Project for Software Quality Assurance

### Objective
The Objective of this project is to integrate software quality assurance activities into an existing Python project. Whatever we learned from our workshops will be integrated in the project.

### Team Members
- Brayden Simpson
- Ian Larson
- Matthew Ippolito
- Melvin Moreno

### Tasks/TODO
1. Create a Git Hook that will run and report all security weaknesses in the project in a CSV file whenever a Python file  is changed and commited. (DONE)
2. Create a 'fuzz.py' file that will automatically fuzz 5 Python methods of your choice. Report any bugs you discovered by the 'fuzz.py' file. 'fuzz.py' will be automatically executed from GitHub actions.
3. Integrate forensics by modifying 5 Python methods of our choice.
4. Report our activities and lessons learned.

### Instructions
#### Git Hook Instructions
1. Modify files in your project.
2. Git add the files.
3. Git commit and see the pre-commit hook run.
4.a. The git hook will run the security analysis. This results in it showing "bandit...........Failed" in the terminal. This means that bandit found a security weakness and wants you to fix it before you can commit and push changes.
4.b. If you want to ignore the security weakness, you can use the `--no-verify` flag when you commit. This will allow you to commit and push changes without fixing the security weakness.
5. Check the CSV file for the results.

### Deadline
May 01, 2023
