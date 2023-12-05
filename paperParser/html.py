import os
import re
from django.urls import reverse
class Html:
    headingTag={
        '###### ':('<h6 id="%s">','</h6>'),
        '##### ':('<h5 id="%s">','</h5>'),
        '#### ':('<h4 id="%s">','</h4>'),
        '### ':('<h3 id="%s">','</h3>'),
        '## ':('<h2 id="%s">','</h2>'),
        '# ':('<h1 id="%s">','</h1>'),
    }
    overlineTag=("<span class='overline'>","</span>")
    highliteTag=("<span class='heighlite'>","</span>")
    codeTag=("<pre><code class='language-%s line-numbers' data-download-link>","</code></pre>")
    aTag=("<a href='%s'>","</a>")
    olTag=("<ol><li>","</li></ol>")
    ulTag=("<ul>","</ul>")
    liTag=("<li>","</li>")
    checkboxTag="<input type='checkbox' checked id='%s'>"
    hruleTag="<hr>"
    divTag=("<div id='%s'>","</div>")
    labelTag=("<label for='%s'>","</label>")
    boldTag=("<span class='bold'>","</span>")
    extLinkTag=('<a href="%s">','</a>')
    pageLinkTag=('<a href="%s" class="page">','</a>')
    italicTag=("<span class='italic'>","</span>")

    def __init__(self,filename:str):
        file=open(filename)
        filer=file.read()
        self.html=[]
        self.title(file,filer)
        file.close()
        filer=filer.split('\n')
        self.fileIter=filer.__iter__()
        self.end=0
    def title(self,fileobj:open,file:str):
        title=re.findall('^# (.*)',file)
        
        if title:
            self.Title=title[0] 
        else:
            self.Title=fileobj.name.split('/')[-1][:-3]
            self.html.append(self.headingTag["# "][0]%self.Title + self.Title + self.headingTag["# "][1])
    def isHeading(self,text:str)->bool:
        '''checks weather the sting given is an heading'''
        return True if text[0:1]=="#" else False
    def isEmbeded(self,text:str)->bool:
        '''check that if the lie starts with ![[(embedded)'''
        return True if re.search('!\[\[.*\]\]',text) else False
    def isImg(self,text:str)->bool:
        return True if text.split('.')[-1] in ('jpeg','jpg','tiff','bmp','png','gif','psd','ai','raw','svg') else False
    def isVideo(self,text:str)->bool:
        return True if text.split('.')[-1]in ('mp4','mov','wmv','avi','avchd','swf','flv','f4v','mkv','webm') else False
    def isAudio(self,text:str)->bool:
        return True if text.split('.')[-1] in ('mp3','aac','aifc','wma','ogg') else False
    def isCode(self,text:str)->bool:
        return True if re.search('^```',text) else False
    def isHRule(self,text:str)->bool:
        '''check weter the line is horizontal rule'''
        return True if '---' == text[0:3] else False
    def isCheckBox(self,text:str):
        return True if '- [ ] ' in text or '- [x] ' in text else False
    def hasInLine(self,text:str)->bool:
        if re.search('\*\*([^\s]+)',text):
            return True
        elif re.search('\*([^\s]+)',text):
            return True
        elif re.search('==([^\s]+)',text):
            return True
        elif re.search('\[.*\]\(.*\)',text):
            return True
        elif re.search('\[\[.*\]\]',text):
            return True
        elif re.search('~~([^\s]+)~~',text):
            return True
        return False
    def hasHighlite(self,text:str)->bool:
        return True if re.search('==([^\s]+)',text) else False
    def hasLink(self,text:str)->bool:
        return True if re.search('\[\[.*\]\]',text) else False
    def hasBold(self,text:str)->bool:
        return True if re.search('\*\*([^\s]+)',text) else False
    def hasItalic(self,text:str)->bool:
        return True if re.search('\*([^\s]+)',text) else False
    def hasOverLine(self,text:str)->bool:
        return True if re.search('~~([^\s]+)~~',text) else False
    def img(self,text:str):
        return "img=%s"%text
    def video(self,text:str):
        return "video=%s"%text
    def head(self,text:str):
        for marker in Html.headingTag:# marker=## Heading
            if marker in text:
                return text.replace(marker,Html.headingTag[marker][0]%text.strip(marker).replace(' ','-') )+Html.headingTag[marker][1]
    def code(self,text:str):
        if self.end and text[:3]=='```':
            self.end=0
            return Html.codeTag[1]
        elif self.end==0 and text[:3]=='```':
            self.html.append(Html.codeTag[0]%text[3:])
            self.end=1
        else:
            if self.text=='':
                pass
            else:
                text=text.replace("<",'&lt')
                text=text.replace('>','&gt')
                self.html.append(text)
        return self.code(self.fileIter.__next__())
        

    def bold(self,text:str):
        mdtag=re.findall('\*\*[^\s].*?\*\*',text)
        word=re.findall('\*\*([^\s].*?)\*\*',text)
        for tag,wor in zip(mdtag,word):
            word=word=Html.boldTag[0]+wor+Html.boldTag[1]
            text=text.replace(tag,word)
        return text
    def highlite(self,text:str):
        mdtag=re.findall('==[^\s].*?==',text)#findig whole tag
        word=re.findall('==([^\s].*?)==',text)#extracting words without tags
        for tag,wor in zip(mdtag,word):
            word=word=Html.highliteTag[0]+wor+Html.highliteTag[1]
            text=text.replace(tag,word)
        return text
    def overline(self,text:str):
        mdtag=re.findall('~~[^\s].*?~~',text)
        word=re.findall('~~([^\s].*?)~~',text)
        for tag,wor in zip(mdtag,word):
            word=word=Html.overlineTag[0]+wor+Html.overlineTag[1]
            text=text.replace(tag,word)
        return text
    def extLink(self,text:str):
        tags=re.findall('\[.*\]\(.*\)',text)
        for word in tags:
            data=word.split('](')
            data=Html.extLinkTag[0]%(data[1])[:-1]+Html.extLinkTag[1]
            text.replace(word,data)

    def embedPaper(self,text:str):
        pass
    def horiRule(self,text:str):
        return '<hr>'
    def italic(self,text:str):
        mdtag=re.findall('\*[^\s].*?\*',text)
        word=re.findall('\*([^\s].*?)\*',text)
        for tag,wor in zip(mdtag,word):
            word=Html.italicTag[0]+wor+Html.italicTag[1]
            text=text.replace(tag,word)
        return text
    def linkPaper(self,text:str):
        mdtag=re.findall('\[\[[^\s].*\]\]',text)
        word=re.findall('\[\[(.*)\]\]',text)
        for tag,wor in zip(mdtag,word):
            link=reverse('paperapi:sendfile',args=['o'])[:-1]+wor.strip()#concatinate page url(getting from reverse function) with pagename 
            atag=(Html.pageLinkTag[0]%link)+wor+Html.pageLinkTag[1]
            text=text.replace(tag,atag)
        return text

    def checkBox(self,text:str):
        if '- [ ] ' in Html.to_html.text:
            return text.replace('- [ ] ','<input type="checkbox" >')
        elif '- [x] ' in Html.to_html.text:
            return text.replace('- [x] ','<input type="checkbox" checked>')
    def convertToHtml(self):
        self.text=self.fileIter.__next__()
        if self.isHeading(self.text):
            self.html.append(self.head(self.text))
        elif self.isEmbeded(self.text):
            self.text=re.findall('!\[\[(.*)\]\]',self.text)[0].replace(' ','_').replace('~','')
            if self.isImg(self.text):
                self.html.append(self.img(self.text))
            elif self.isVideo(self.text):
                self.html.append(self.video(self.text))
        elif self.isCode(self.text):
            self.html.append(self.code(self.text))
        elif self.isHRule(self.text):
            self.html.append(self.horiRule(self.text))
        elif self.isCheckBox(self.text):
            self.html.append(self.checkBox(self.text))
        elif self.hasInLine(self.text):
            if self.hasLink(self.text):
                self.text=self.linkPaper(self.text)
            if self.hasBold(self.text):
                self.text=self.bold(self.text)
            if self.hasOverLine(self.text):
                self.text=self.overline(self.text)
            if self.hasItalic(self.text):
                self.text=self.italic(self.text)
            if self.hasHighlite(self.text):
                self.text=self.highlite(self.text)
            #appending the processed version
            self.html.append(self.text)
        else:
                self.html.extend([self.text])
        try:
            self.html.append('<br>')
            self.convertToHtml()
        except StopIteration:
            pass

    def __str__(self):
        pass

