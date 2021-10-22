from download import DownloadFile 


file_url = input('paste url for dowanload...')


download = DownloadFile(file_url)

download.download()