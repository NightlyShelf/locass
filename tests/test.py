from src.locass import locass
locass.configure("./test-locals/", {"RU": "ru.lang", "EN": "en.lang"}, "[k]", "[v]")
locass.loadLang("RU")
print(locass.g("HW!"))