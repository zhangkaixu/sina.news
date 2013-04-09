#!/usr/bin/python3
import re
import sys


def gen_doc(file):
    dc=0
    for line in file:

        line=line.strip()
        if line==b'<doc>' :
            doc=[]
            meta=[]
            continue
        if line.startswith(b'<url>'):
            url=line
            continue
        if line.startswith(b'<meta')or line.startswith(b'<title>'):
            if b'charset' in line :
                line2=line.decode()
                charset=re.search(r'charset=([^\"]+)\"',line2).group(1)
                #continue
            meta.append(line)

        if line==b'</doc>' :
            if charset=='gb2312' or charset=='GB2312':
                url=url[5:-6].decode()
                doc=list(map(lambda x:x.decode('utf8',errors='ignore'),doc))
                meta=list(map(lambda x:x.decode('utf8',errors='ignore'),meta))
            elif charset=='utf-8' :
                continue
            else :
                continue
            


            isc=False
            mk=False
            content=[]
            for line in doc:
                if line.startswith('<!-- publish_helper name'):
                    isc=True
                    mk=True
                    dc+=1
                    continue
                if line == '<!-- publish_helper_end -->'  :
                    isc=False
                    break
                if isc : content.append(line)

            if mk==False :
                for line in doc:
                    if line == '<!-- 正文内容 begin -->'  :
                        isc=True
                        mk=True
                        dc+=1
                        continue
                    if line == '<!-- 正文内容 end -->'  :
                        isc=False
                        break
                    if isc : content.append(line)

            #print(mk,dc)

            content=[x for x in content if x]
            if content :
                yield url,meta,content
        doc.append(line)


if __name__ == '__main__':
    #filename='2012.07.pages'
    #file=open(filename,'rb')
    sys.stdin = sys.stdin.detach()
    urls=set()
    for url,meta,doc in gen_doc(sys.stdin):
        if url in urls : continue
        print('<doc>')
        print('<url>%s</url>'%url)
        print(*meta,sep='\n')
        print(*doc,sep='\n')
        print('</doc>')
        pass
