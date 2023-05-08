import webbrowser as wbb


def web_automation():
    chrome_patch = "C:\Program Files\Google\Chrome\Application\chrome.exe %s"
    urls = ('apple.com', 'github.com', 'google.bg')

    for url in urls:
        print('Opening: ' + url)
        wbb.get(chrome_patch).open(url)


web_automation()
