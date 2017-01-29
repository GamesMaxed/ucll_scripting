def scrape_html(str):
    pattern = r"""<a href="[^"]*">"""
    return re.findall(pattern, str)
