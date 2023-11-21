from selenium import webdriver


class youtube():
    def __init__(self):
        self.driver = webdriver.Edge(executable_path=r'C:\Users\Deep\Downloads\edgedriver_win64\msedgedriver.exe')

    def play(self, query):
        self.query = query
        self.driver.get(url="https://www.youtube.com/results?search_query=" + query)
        video = self.driver.find_element_by_xpath('//*[@id="dismissible"]')
        video.click()


# assist = youtube()
# assist.play('ruaan')