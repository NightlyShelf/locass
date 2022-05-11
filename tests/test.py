import locass
man = locass.LocalManager()
#man.configure("./test-locals/", {"RU": "ru.lang", "EN": "en.lang"}, "[k]", "[v]")
man.loadLang("RU")
print(man.g("HW!"))
print(man.g("GW!"))