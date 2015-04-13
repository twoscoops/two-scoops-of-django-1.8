"""
Blogged in http://twoscoopspress.com/blogs/news/11935321-the-appendix-that-didnt-survive

This has been modified from the code in that blog example to handle the \linkdiff command.
"""
# getlinks.py
import glob
import re

# Regex to find all the links defined in LaTeX
regex = re.compile(r'\\link[a-z]{0,4}{.*}', re.IGNORECASE)


def strip_http_things(link):
    """Used to clean links for better sorting and for 'cleaner' final
        display:

        e.g. http://www.djangopackages.com is returned as djangopackages.com
        """
    link = link.replace("https://", "").replace("http://", "")
    return link.replace("www.", "")


def cleaned_url_comparison(a, b):
    """This custom sort ensures that the domain is the leading sort, not the
        various protocol prefixes.

        See  http://docs.python.org/2/library/functions.html#sorted"""
    a = strip_http_things(a)
    b = strip_http_things(b)

    if a > b:
        return 1
    if a == b:
        return 0
    return -1


def main():
    tmp = []  # temporary holder for links
    links = []  # results list

    # Find all the LaTeX files in the chapters directory
    for filename in glob.glob("chapters/*.tex"):

        # Open the LaTeX file
        with open(filename) as f:
            text = f.read()

        # Find all the links in the LaTeX file and add them to tmp
        tmp += re.findall(regex, text)

    for link in tmp:
        if ':8000' not in link:  # Ignore the links to port 8000
            link = link.replace("www.2scoops.co", "2scoops.co")
            links.append(link[0:link.index('}') + 1])

    # Remove MOST of the duplicates
    links = list(set(links))

    # Sort the links. See cleaned_url_comparison() above.
    links = sorted(links, cmp=cleaned_url_comparison)

    return links


if __name__ == "__main__":
    with open("links.html", "w") as f:
        text = "<ul>\n"

        for link in main():
            # strip LaTeX elements
            link = link.replace("\link{", "")
            link = link.replace("\linkdiff{", "")
            link = link.replace("}", "")

            # Add to the unordered list
            text += """  <li><a href="{}">{}</a></li>\n""".format(
                link,
                strip_http_things(link)
            )

        text += "</ul>\n"
        f.write(text)
