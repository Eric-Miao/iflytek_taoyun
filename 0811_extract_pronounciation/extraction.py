'''
    @Author:  Yuxin Miao
    @Date:  2020-08-11 11:27:58
    @Last Modified by:  Yuxin Miao
    @Last Modified time:  2020-08-11 11:27:58
'''
import os
import xml.sax


class DictHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.word = None
        self.pronouce = None
        self.pronoucekk = None
        self.pos = None
        self.in_head = False
        self.has_read = False
    
    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == 'Entry':
            print('******* new word *********')
            self.in_head = True
            self.has_read = False


    def endElement(self, tag):
        
        if not self.in_head:
            return

        if tag == 'Head':
            self.in_head = False
            self.has_read = False

        if tag == 'Entry':
            print('*******End********\n')

        if tag == 'PronCodes':
            self.has_read = True
            
        if tag == 'HWD':
            print('word:', self.word)
        elif tag == 'PRON' and self.word == 'abominable': 
            print(self.pronouce)
            quit()

        elif tag == 'PRON' and not self.has_read:   
            print('pron:', self.pronouce)

        elif tag == 'PRONKK'and not self.has_read:
            print('pronkk', self.pronoucekk)
            if self.word == 'abominable':
                quit()
        
    def characters(self, content):
        if not self.in_head:
            return

        if self.CurrentData == 'HWD':
            self.word = content 
        elif self.CurrentData == 'PRON' and not self.has_read:   
            print(content)
            self.pronouce = content
        elif self.CurrentData == 'PRONKK'and not self.has_read:
            self.pronoucekk = content
        # elif self.CurrentData == 'POS':
        #     self.pos = content

if __name__ == "__main__":
    parser = xml.sax.make_parser()

    parser.setFeature(xml.sax.handler.feature_namespaces, 0)

    handler = DictHandler()
    parser.setContentHandler(handler)

    files = os.listdir('data/raw/')
    files.sort()

    parser.parse('data/raw/test.xml')
    # parser.parse('data/raw/'+files[0])