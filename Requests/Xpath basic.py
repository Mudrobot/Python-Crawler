# Xpath是在xml文档中搜索内容的一种语言
# html是xml的一个子集
html="""
<book>
    <id>1</id>
    <name>野花遍地香</name>
    <price>1.23</price>
    <nick>臭豆腐</nick>
    <author>
        <nick id="10086">王者荣耀</nick>
        <nick id="10010">和平精英</nick>
        <nick class="game">原神</nick>
        <nick class="joy">使命召唤</nick>
        <div>
            <nick>真的好玩！！！</nick>
        </div>
    </author>

    <partner>
        <nick id="LBW">卢本伟</nick>
        <nick id="DSM">大司马</nick>
    </partner>
</book>
"""
from lxml import etree
tree=etree.XML(html)
#result=tree.path("/book")
result=tree.xpath("/book/author/*/nick/text()")
print(result)