# 接收url 转为sitemap.xml

import  datetime

NEW_TEMPLATE='''
<url> 
<loc>http://m.example.com/index.html</loc> 
<mobile:mobile type="mobile"/>
<lastmod>2009-12-14</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url> 
<url> 
<loc>http://www.example.com/index.html</loc>
<lastmod>2009-12-14</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url> 
<url> 
<loc>http://www.example.com/autoadapt.html</loc> 
<mobile:mobile type="pc,mobile"/>
<lastmod>2009-12-14</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url> 
<url> 
<loc>http://www.example.com/htmladapt.html</loc> 
<mobile:mobile type="htmladapt"/>
<lastmod>2009-12-14</lastmod>
<changefreq>daily</changefreq>
<priority>0.8</priority>
</url> 
</urlset>
'''

TEMPLATE_PC='''
<url>
<loc>{}</loc>
<lastmod>{}</lastmod>
<changefreq>{}</changefreq>
<priority>{}</priority>
</url>'''

TEMPLATE_MOBILE='''
<url>
<loc>{}</loc>
<mobile:mobile type="mobile"/>
<lastmod>{}</lastmod>
<changefreq>{}</changefreq>
<priority>{}</priority>
</url>'''

class SiteMap():

    def __init__(self,url_list):
        # self.site_map_header='<urlset xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9 http://www.sitemaps.org/schemas/sitemap/0.9/sitemap.xsd">'
        self.site_map_header='''<?xml version="1.0" encoding="UTF-8" ?> 
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
xmlns:mobile="http://www.baidu.com/schemas/sitemap-mobile/1/"> 
'''
        self.site_map_header_end = '</urlset>'
        self.data = url_list
        self.site_map_str = ''
        self.current = datetime.datetime.now().strftime('%Y-%m-%d')

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
        
        ts='{}T00:20:55+00:00'.format(self.current)
        freq='daily'
        priority='0.7'
        each_node_pc = TEMPLATE_PC.format(url,ts,freq,priority)
        each_node_mobile = TEMPLATE_MOBILE.format(url,ts,freq,priority)
        return each_node_pc+each_node_mobile
        
