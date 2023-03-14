layout = [[sg.T('Source Folder')],
              [sg.In(key='input')],
              [sg.FolderBrowse(target='input'), sg.OK()]]