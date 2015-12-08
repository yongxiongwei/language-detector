#-*- coding: utf-8 -*-
# download test from http://www.statmt.org/europarl/v7/es-en.tgz
from os.path import dirname, realpath
from os import listdir
from timeit import timeit

directory_of_this_file = dirname(realpath(__file__))
directory_of_sources = directory_of_this_file[:-6] + "/prep/sources"
 
print timeit('''
    from language_detector import detect_language
    from os import listdir
    directory_of_sources = "''' + directory_of_sources + '''"
    languages = [f for f in listdir(directory_of_sources) if not f.startswith("_")]
    number_of_files = 0
    errors = 0
    for language in languages:
        directory_of_language_files = directory_of_sources + "/" + language
        for filename in listdir(directory_of_language_files):
            filepath = directory_of_language_files + "/" + filename 
            with open(filepath) as f:
                text = f.read().decode("utf-8")
                number_of_files += 1
                errors += detect_language(text) != language
    print "% errors are", float(errors) / number_of_files

''', number = 10)

print timeit('''
    d = {}
    d['ar'] = "Arabic"
    d['en'] = "English"
    d['es'] = "Spanish"
    d['fr'] = "French"
    d['ku'] = "Kurdish"
    d['ru'] = "Russian"
    d['tr'] = "Turkish"
    d['zh'] = "Mandarin"

    from langid import classify
    from os import listdir
    directory_of_sources = "''' + directory_of_sources + '''"
    languages = [f for f in listdir(directory_of_sources) if not f.startswith("_")]
    number_of_files = 0
    errors = 0
    for language in languages:
        directory_of_language_files = directory_of_sources + "/" + language
        for filename in listdir(directory_of_language_files):
            filepath = directory_of_language_files + "/" + filename 
            with open(filepath) as f:
                text = f.read().decode("utf-8")
                number_of_files += 1
                code = classify(text)[0]
                if code in d and d[code] == language:
                    pass
                else:
                    errors += 1
    print "% errors are", float(errors) / number_of_files

''', number = 10)
