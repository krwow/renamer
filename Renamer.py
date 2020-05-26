''' 
"Renamer" is a tiny text-based application written in Python for batch files renaming in selected folder.
It removes the whole text from filenames located before the phrase entered in application.

Author: Krzysztof Wowczeniuk.
'''

class prefix_remover(object):
    '''
    Main class of application.
    '''

    def start(self):
        '''
        Starts application.
        '''
        import os
        run = True
    
        while run == True:

            valid_path = False
            while valid_path == False:
                input_path = input('Please enter the path to a folder with files to rename (e.g. "C:\\Users\\Default\\Desktop"): ')
                input_path = input_path.replace('"', '')
                valid_path = os.path.isdir(input_path)
                if valid_path == False:
                    print('Please enter the valid directory.')

            valid_text = False
            while valid_text == False:
                input_text = input('Please enter the text which will be the beginning of target filenames (case sensitive): ')
                input_text = input_text.strip()
                if input_text:
                    valid_text = True
                else:
                    print('Please enter any text.')

            dot = '.'
            total = 0
            changed = 0
            file_exceptions = ['desktop.ini', 'thumbs.db']

            for filename_input in os.listdir(input_path):
                filename_list = filename_input.rsplit(dot, 1)
                if filename_input not in file_exceptions:
                    total = total + 1
                    print('Filename:', filename_input)
                    start_nr = filename_list[0].find(input_text)
                else:
                    start_nr = -1

                if start_nr != -1 and start_nr != 0:
                    result = filename_list[0][start_nr:]
                    result = result.strip()
                    rename_input = os.path.join(input_path, filename_input)
                    filename_output = result + dot + filename_list[1]
                    rename_output = os.path.join(input_path, filename_output)
                    try:
                        os.rename(rename_input, rename_output)
                        print('Filename after the change:', filename_output)
                        changed = changed + 1
                    except:
                        print('Cannot access the file or different file with identical target name already exists:', filename_input)

            print('Number of files in folder:', total)
            print('Number of files with changed filename:', changed)
            end = input('If you would like to change the filenames of other files, please enter "t" and press "Enter". If you would like to EXIT the application, just press "Enter": ')
            end = str(end)
            end = end.lower()
            if end != 't':
                run = False

if __name__ == '__main__':
    app = prefix_remover()
    app.start()