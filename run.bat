C:\Users\shenl\PycharmProjects\nopcommerceApp\.venv\Scripts\pytest.exe -s -v -m "sanity" --html=./Reports/report_chrome.html testCases/ --browser chrome

rem C:\Users\shenl\PycharmProjects\nopcommerceApp\.venv\Scripts\pytest.exe -s -v -m "sanity" --html=./Reports/report_firefox.html testCases/ --browser firefox
rem C:\Users\shenl\PycharmProjects\nopcommerceApp\.venv\Scripts\pytest.exe -s -v -m "sanity or regression" --html=./Reports/report.html testCases/ --browser chrome
rem C:\Users\shenl\PycharmProjects\nopcommerceApp\.venv\Scripts\pytest.exe -s -v -m "sanity and regression" --html=./Reports/report.html testCases/ --browser chrome
rem C:\Users\shenl\PycharmProjects\nopcommerceApp\.venv\Scripts\pytest.exe -s -v -m "regression" --html=./Reports/report.html testCases/ --browser chrome
