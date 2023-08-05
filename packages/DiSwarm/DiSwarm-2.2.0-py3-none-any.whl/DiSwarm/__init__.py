import DiSwarm._interface as inter
import DiSwarm.keydet as kd
from cryptography.fernet import Fernet
from time import time, sleep

name = 'DiSwarm'

class Swarm:
    def __init__(self, channel_id, bot_tok, swarm_id, bot_id):
        self.swarm, self._thread = inter.swarm_begin(bot_tok, channel_id)
        self.key = kd.detkey(bot_tok,channel_id)
        self.id = str(swarm_id)
        self.bid = str(bot_id)
        print(self.key)
        #print(self.key)
    def send(self, msg):
        crypt = Fernet(self.key)
        crypted = str(crypt.encrypt(bytes(str(msg), 'utf-8')))
        crypted = crypted[2:len(crypted)-1]
        inter.pipe.put('\n'.join([str(time()),self.id,self.bid,crypted]))
    def get_queue(self):

        crypt = Fernet(self.key)
        decrypted = []
        for i in inter.pipe.get():
            sp = i.split('\n')
            if sp[1] == self.id and sp[2] != self.bid:
                dec = str(crypt.decrypt(bytes(sp[3],'utf-8')))
                decrypted.append((float(sp[0]),dec,sp[2]))
        return decrypted
    def end(self):
        inter.end()


'''s = Swarm('nope','heck no','example id')
s.send(b'test')
sleep(5)
print(s.get_queue())
s.end()'''
