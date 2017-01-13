def scrapeHtml(str):
    pattern = r"""<a href="[^"]*">"""
    return re.findall(pattern, str)
