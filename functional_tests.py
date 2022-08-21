from selenium import webdriver

print("Hello 123")
browser = webdriver.Firefox()
browser.get('http://localhost:8000')

assert 'Django' in browser.title
