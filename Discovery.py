import os 

def discover(initial_path):
    extensions = [
        #'jpg', 'jpeg', 'txt', 'img', 'html', 'png', 'csv', 'pdf'
        'pdf', 'jpeg'
    ]


    for dirpath, dirs, files in os.walk(initial_path):
        for _file in files:
            absolut_path = os.path.abspath(os.path.join(dirpath, _file))
            ext = absolut_path.split('.')[-1]
            if ext in extensions:
                yield absolut_path

if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)