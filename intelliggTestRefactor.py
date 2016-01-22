#!/usr/local/bin/python3

import unittest
import validators
import urllib.request
import re

class urlDescriptor(object):
    def __init__(self,initialValue="http://www.computerworld.co.uk"):
        self.value = initialValue
    def __get__(self,instance,owner):
        print("1 - urlGet")
        return self.value
    def __set__(self,instance,value):
        print("2 - urlSet")
        if not validators.url(value):
            raise AttributeError("Bad url.")
        self.value = value

class wordDescriptor(object):
    def __init__(self,initialValue=""):
        self.value = initialValue
    def __get__(self,instance,owner):
        print("3 - wordGet")
        return self.value
    def __set__(self,instance,value):
        print("4 - wordSet")
        if not isinstance(value,str):
            raise AttributeError("Value must be string.")
        self.value = value

class Counter(object):
    def __init__(self,counterURL="http://www.computerworld.co.uk",counterWord=""):
        self.__url = counterURL
        self.__word = counterWord
    def GetPage(self):
        request = urllib.request.Request(self.url.__get__(self,Counter))
        response = urllib.request.urlopen(request)
        source = response.read()
        return str(source)
    def CountInText(self,text):
        pattern = re.compile(r'\Wcloud\W') # I modified the pattern. Now, entries like cloud) or cloud. will also be matched.
        iterable = re.finditer(pattern, text)
        return sum([1 for match in iterable])
    def Count(self):
        return self.CountInText(self.GetPage())
    url = urlDescriptor(initialValue=counterURL)
    word = urlDescriptor(initialValue=counterURL)


class TestURLDescriptor(unittest.TestCase):
    def test_hasInit(self):
        desc = urlDescriptor()
        self.assertTrue("__init__" in dir(desc))
    def test_hasGet(self):
        desc = urlDescriptor()
        self.assertTrue("__get__" in dir(desc))
    def test_hasSet(self):
        desc = urlDescriptor()
        self.assertTrue("__set__" in dir(desc))

class TestCounter(unittest.TestCase):
    def test_hasURL(self):
        counter = Counter()
        self.assertTrue(hasattr(counter,"url"))
    def test_hasWord(self):
        counter = Counter()
        self.assertTrue(hasattr(counter,"word"))
    def test_GetPageReturnsString(self):
        counter = Counter()
        self.assertTrue(isinstance(counter.GetPage(),str))
    def test_CountInTextReturnsInt(self):
        counter = Counter()
        text = ""
        self.assertTrue(isinstance(counter.CountInText(text),int))
    def test_CountReturnsInt(self):
        counter = Counter()
        self.assertTrue(isinstance(counter.Count(),int))


if __name__ == "__main__":
    counter = Counter()
    print(counter.url)
    #print("Matches for cloud: "+str(counter.Count()))
    #unittest.main()
