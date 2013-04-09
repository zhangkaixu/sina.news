#!/usr/bin/python3
import re
import sys


def gen_doc(file):
    for line in file:
        line=line.strip()
        if line=='<doc>' :
            doc=[]
            meta=[]
            continue
        if line.startswith('<url>'):
            url=line
            continue
        if line.startswith('<meta')or line.startswith('<title>'):
            meta.append(line)

        if line=='</doc>' :
            content=[]
            for line in doc :
                r=re.search(r'<p>(.*)</p>',line)
                if r :
                    content.append(r.group(1).strip())
            yield url,meta,content
        doc.append(line)


if __name__ == '__main__':
    urls=set()
    for url,meta,doc in gen_doc(sys.stdin):
        if url in urls : continue
        urls.add(url)
        print('<doc>')
        print(url)
        print(*meta,sep='\n')
        print(*doc,sep='\n')
        print('</doc>')
        pass
