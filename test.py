import bpcs

alpha = 0.01
vslfile = './examples/vessel.png'
msgfile = './examples/message.txt'  # can be any type of file
encfile = './examples/output.png'
msgfile_decoded = './examples/decoded.txt'

# check max size of message you can embed in vslfile
# bpcs.encoderClass(vslfile, "", "", alpha).getCapacity()
# # embed msgfile in vslfile, write to encfile
bpcs.encoderClass(vslfile, msgfile, encfile, alpha).encode()
# recover message from encfile
bpcs.decoderClass(encfile, msgfile_decoded, alpha).decode()
