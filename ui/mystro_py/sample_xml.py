
from mako.template import Template
from mako.runtime import Context
#<p>${i}</p>
tpl_xml = '''<?xml version="1.0" ?>
<AssetLists>
% for i in data:
<Asset>
<Title>${i[0]}</Title>
<OfferingId>${i[1]}</OfferingId>
</Asset>
% endfor
</AssetLists>
'''
titleList=[]

for i in range(0,100000):
    tup=(str(i),str(i))
    titleList.append(tup)    
#tup1=("Episod1","Episod1 offerinf")

#titleList.append(tup1)

titleLed=len(titleList)

tpl = Template(tpl_xml)

with open('output.xml', 'w') as f:
    ctx = Context(f, data=titleList)
    tpl.render_context(ctx)

