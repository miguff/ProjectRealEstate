from seleniumbase import Driver

class DataDownload():
    def __init__(self) -> None:
        self.driver = Driver(uc=True, headless=True)

    def HTMLDownloader(self, URL):

        self.driver.uc_open_with_reconnect(URL, 4)
        self.driver.sleep(3)
        content = self.driver.page_source
        file_path = "output.html"
        print(content)
        # Write the content to the HTML file
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    def Driverclose(self):
        self.driver.quit()