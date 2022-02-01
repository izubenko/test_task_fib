# Test task

1. Go to project folder using terminal
2. Activate test environment, type at terminal: source env/bin/activate
3. Should be (env) at beginning terminal
4. Upadte pip, type at terminal: pip install -U pip
5. Install requirements, type at terminal: pip install -r requirements.txt

To run all autotests type at terminal: pytest

To run UI autotests in different browsers, use the command at terminal:
For Chrome: pytest --browser_name=chrome
For Firefox: pytest --browser_name=firefox
The default is chrome