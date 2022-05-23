
from url_source import DataSource
from sitemap_creator import SiteMap


def main():
    url = DataSource()
    _url=url.run()
    sitemap = SiteMap(_url)
    sitemap.gen()


if __name__=='__main__':
    main()