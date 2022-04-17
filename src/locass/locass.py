"""
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Simple Localization Manager writed on Python
version 1.0
Copyright © Shchur Artem 2022
License: MIT License
Source code: Available on Github
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to use:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 1: Create a folder with your localization files and add path to it on variable PATH below
Step 2: Create localization files using your own markers or use default, markdown is:
KEYMARKER(keyvalue)VALUEMARKER(value)
for example:
[k]HW![v]Привет Мир!
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
How to use in your project:
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Step 1: Import this module in your project;
Step 2: Configure module, using configure() function.
First argument is the path, where your localization files are, for example "./test-test-locals/"
NOTE: Please, don't lose "/" symbols!
Second argument is the dictionary, which contains the localization name as a key and name of file as a value, for example {"RU": "ru.lang", "EN": "en.lang"}
Third is the Keymarker of your markdown you used in localization files, for example "[k]"
Last is the Valuemarker of your markdown, for example "[v]"

So if you used next markdown of localization flies:
file ru.lang in ./test-test-locals/ with inside
[k]HW![v]Привет Мир!
and file en.lang in the same directory with inside
[k]HW![v]Hello World!
your call will be like:
configure("./test-test-locals/",{"RU": "ru.lang"},"[k]","[v]")

Step 3: Load language, using loadLang(key), where key is key of language you declared in configured dictionary, for example:
loadLang("EN")
of course, you can reload it to change the language later

And now you can use it freely, to get the word ot phrase from localization, only use g(key), where key is key you declared
in your localization file. For example:
g("HW!") //returns Привет Мир!
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
Have a nice coding!
"""

#NOTE: Here is default and TEST-only values, they will be changed after configure() call
Path = "test-test-locals/"
Langs = {"RU": "ru.lang", "EN": "en.lang"}
Keymarker = "[k]"
Valuemarker = "[v]"

langvalue = None


def loadLang(key):
    """
    Loading selected localization to use-in
    :param key: Key to selected localization, declared in Langs
    :return: None
    """
    global langvalue
    try:
        path = Langs.get(str(key))
    except:
        print("[ERROR] Invaild language key. Try to reinstall the application.")
        exit(1)
    try:
        obj = open(Path + path, "r")
        langvalue = obj.readlines()
        obj.close()
    except FileNotFoundError:
        print("[ERROR] Couldn't load localization file. Try to reinstall the application. Details: Cannot found", path)
        exit(1)


def configure(path, langs, keym, valuem):
    global Path
    global Langs
    global Valuemarker
    global Keymarker
    Path = path
    Langs = langs
    Valuemarker = valuem
    Keymarker = keym


def g(key):
    """
    Returning selected by key parameter phrase from selected localization
    :param key: Key to phrase, declared in localization
    :return: Selected phrase from localization
    """
    if (langvalue == None):
        print("[ERROR] Couldn't load localization. Try to reinstall the application.")
        exit(1)
    word = None
    for line in langvalue:
        if (Keymarker + key + Valuemarker in line):
            word = line[len(key) + 6:]
            break
    if (word == None):
        print(
            "[ERROR] Couldn't load correct word in selected localization. Try to change another language or reinstall the application. Details: requested key:", key)
    else:
        word = word[:len(word) - 1]
        return word


def Generator():
    pass

