from bs4 import BeautifulSoup 
html = """
<html><head><title>Python Language</title></head>
<body>
<div class="toctree-wrapper compound">
<li class="toctree-l1"><a class="reference internal" href="introduction.html">1. Introduction</a>
<ul>
<li class="toctree-l2"><a class="reference internal" href="introduction.html#alternate-implementations">1.1. Alternate Implementations</a></li>
<li class="toctree-l2"><a class="reference internal" href="introduction.html#notation">1.2. Notation</a></li>
</ul>
</li>
<li class="toctree-l1"><a class="reference internal" href="lexical_analysis.html">2. Lexical analysis</a>
<ul>
<li class="toctree-l2"><a class="reference internal" href="lexical_analysis.html#line-structure">2.1. Line structure</a></li>
<li class="toctree-l2"><a class="reference internal" href="lexical_analysis.html#other-tokens">2.2. Other tokens</a></li>
<li class="toctree-l2"><a class="reference internal" href="lexical_analysis.html#identifiers">2.3. Identifiers and keywords</a></li>
<li class="toctree-l2"><a class="reference internal" href="lexical_analysis.html#literals">2.4. Literals</a></li>
<li class="toctree-l2"><a class="reference internal" href="lexical_analysis.html#operators">2.5. Operators</a></li>
<li class="toctree-l2"><a class="reference internal" href="lexical_analysis.html#delimiters">2.6. Delimiters</a></li>
</ul>
</li>
</div>
</body>
</html>
"""
soup = BeautifulSoup(html, 'html.parser')
#head标签
print(soup.head.string)
#获取第一个超链接信息
firstlink = soup.a
#打印链接地址
print(firstlink['href'])
#获取所有的超链接信息
links = soup.find_all('a')
#打印每个超链接对应的链接信息
for link in links:
	print('href=',link['href'],"link=",link.string)



