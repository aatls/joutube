def trim_link(link):
    if "=" in link:
        return link.rsplit("=")[1].rsplit("?")[0].rsplit("&")[0].rsplit("#")[0]
    else:
        return ""