import hashlib
class Hash:
    def sha256(self,word):
        hs = hashlib.sha256(word.encode('utf-8')).hexdigest()
        return hs
    def md5(self,word):
        m = hashlib.md5()
        m.update(word.encode('utf-8'))
        return m.hexdigest()
class File:
    def load_words(self,hash,file):
        hash_maker = Hash()
        print("[+] Cracking started")
        with open(file,"r", encoding='ISO-8859-1') as infile:
            for line in infile:
                print("[+] Trying "+line)
                flag = 0
                if(hash_maker.sha256(line) == hash):
                    print("[+] hash fount \n[*] type: sha256\n[*] Word : "+str(line))
                    flag = 1
                if(hash_maker.md5(line) == hash):
                    print("[+] hash fount \n[*] type: md5\n[*] Word : "+str(line))
                    flag = 1
                if(flag == 1):
                    quit()
                
file = File()
file.load_words('5f4dcc3b5aa765d61d8327deb882cf99','realuniq.lst')
