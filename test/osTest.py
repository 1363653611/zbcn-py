import os

if __name__ == '__main__':
    baseDir = os.getcwd() + '/logs/gunicorn/'
    if not os.path.exists(baseDir):
        os.makedirs(baseDir)
