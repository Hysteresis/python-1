from extract import Extract


url = "https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/"

extractor = Extract("https://www.laboitedufromager.com/liste-des-fromages-par-ordre-alphabetique/")
extractor.read_website()
