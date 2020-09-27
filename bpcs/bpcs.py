from imageClass import imageClass
from messageClass import messageClass
from encodeClass import encoderClass
from decodeClass import decoderClass


alpha = 0.45
vslfile = 'files/vessel.png'
msgfile = 'files/message.txt'  # Accepts strings too
encfile = 'files/encoded.png'
msgfile_decoded = 'files/output.txt'


en = encoderClass(vslfile, msgfile, encfile, alpha)
de = decoderClass(encfile, msgfile_decoded, alpha)

en.getCapacity()
en.encode()  # This checks max size of message before attempting to embed
de.decode()
