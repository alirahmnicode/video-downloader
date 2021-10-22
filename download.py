import requests

class DownloadFile:
    def __init__(self , url):
        self.url = url
        self.downloaded_size = 0
    
    def download(self):
        r = requests.get(self.url , stream=True)
        file_size = int(r.headers['content-length'])
        with open('a.mp4', 'wb') as fd:
            print('download..')
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
                self.downloaded_size += len(chunk)
                done = int(50*self.downloaded_size/file_size)
                print("\r[%s%s]" % ('=' * done, ' ' * (50-done)), end='')
                
