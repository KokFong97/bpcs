from .imageClass import imageClass
from .messageClass import messageClass
from .encodeClass import encoderClass
from .decodeClass import decoderClass


alpha = 0.45
vslfile = 'bpcs/files/vessel.png'
msgfile = 'bpcs/files/message.txt'  # Accepts strings too
encfile = 'bpcs/files/encoded.png'
msgfile_decoded = 'bpcs/files/output.txt'

# check max size of message you can embed in vslfile
en = encoderClass(vslfile, msgfile, encfile, alpha)
de = decoderClass(encfile, msgfile_decoded, alpha)

en.getCapacity()
en.encode()
de.decode()
