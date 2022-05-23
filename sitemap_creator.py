# 接收url 转为sitemap.xml


TEMPLATE='''
<url>
<loc>{}</loc>
<lastmod>{}</lastmod>
<changefreq>{}</changefreq>
<priority>{}</priority>
</url>'''
class SiteMap():

    def __init__(self,url_list):
        self.site_map_header='<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">'
        self.site_map_header_end = '</urlset>'
        self.data = url_list
        self.site_map_str = ''

    def gen(self):
        self.site_map_str+=self.site_map_header
        for url in self.data:
            self.site_map_str+=self.node(url)

        self.site_map_str+=self.site_map_header_end
        self.write_file(self.site_map_str)

    def write_file(self,content):
        with open('sitemap.xml','w') as fp:
            fp.write(content)


    def node(self,url):
        ts='2022-05-23T08:23:55+00:00'
        freq='daily'
        priority='0.7'
        each_node = TEMPLATE.format(url,ts,freq,priority)
        return each_node
        
