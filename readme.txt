Key Features of this framework
Selenium web driver with Python
Pytest
Page object model
Log fie for each run
Allure reporting plus screeshot on failure 6.Utility files for common method
Property files.
Conftest file for setup and teardown.

Test case : Test_Recarga.py
Pages:
Home_Screen.py
Checkout_Screen.py


Tto run the code without generating report

command : pytest -s -v Test_Recarga.py

Run code and generate report in report directory
command 1 : pytest -s -v  --alluredir=../reports Test_Recarga.py
command 2 : allure serve D:\Undostres_Automation\reports

Run cross broswer testing with below command
pytest -s -v --browserName=chrome/firefox  --alluredir=../reports Test_Recarga.py





