from __future__ import unicode_literals
import tableauserverclient as TSC


#Enter log in credentials and server URL.

import sys, os , codecs
from pprint import pprint
tableau_auth = TSC.TableauAuth('username', 'passcode', 'SITE')
server = TSC.Server('server path', use_server_version=True)



# function that downloads all workbooks from server that start with xxxx
def download_all_MID_workbooks(server,download_dir):
    all_MAS_workbooks = list(wb for wb in TSC.Pager(server.workbooks) if wb.name.startswith('xxxx'))
    for MAS_workbook in all_xxxx_workbooks:
        wb_download_dir = os.path.join(download_dir,xxx_workbook.project_name)
        if not os.path.exists(wb_download_dir):
            os.makedirs(wb_download_dir)
        path = server.workbooks.download(MAS_workbook.id, filepath=wb_download_dir,include_extract=True)
        print("Downloaded workbook to {}".format(path))
		

# Call the function to download all MAS workbooks from server.
with server.auth.sign_in(tableau_auth):
    download_all_xxxx_workbooks(server, "Workbooks")
                
