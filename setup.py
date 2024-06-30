from http.client import FOUND
import os

#######################################################################
print("checking for django in your pc ....")
try:
    import django
    print("Django is installed ..... Moving on to the next library")
except ModuleNotFoundError:
    print("django installation not found!")
    print("Installing Django ...")
    os.system("pip install django")
    os.system("pip install django-clearcache")
#######################################################################

#######################################################################
print("checking for pymysql ...")
try:
    import pymysql
    print("pymysql is already installed!")
except ModuleNotFoundError:
    print("pymysql installation not found!")
    print("Installing pymysql ...")
    os.system('pip install pymysql')
#######################################################################

#######################################################################
print("Checking For tensorflow installation")
try:
    import tensorflow
    print("tensorflow is already installed!")
except:
    print("Tensorflow installation not found!")
    print("Installing Tensorflow ...")
    os.system('pip install --user tensorflow')
#######################################################################

#######################################################################
print("Checking For tflearn installation")
try:
    import tensorflow
    print("tflearn is already installed!")
except:
    print("TfLearn installation not found!")
    print("Installing TfLearn ... May Take a While!")
    os.system('pip install tflearn')
#######################################################################

#######################################################################
print("Checking For Numpy installation")
try:
    import tensorflow
    print("Numpy is already installed!")
except:
    print("Numpy installation not found!")
    print("Installing Numpy ...")
    os.system('pip install numpy')
#######################################################################

#######################################################################
print("Checking For NLTK installation")
try:
    import tensorflow
    print("NLTK is already installed!")
except:
    print("NLTK installation not found!")
    print("Installing NLTK ...")
    os.system('pip install --user nltk')
    print("Installing NLTK Libraries now .... This may take a while!")
    os.system('python -m nltk.downloader all')
#######################################################################

print("Your Setup is complete ... carry on with the next step")