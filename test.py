import bpcs

alpha = 0.45
vslfile = 'examples/test2.png'
msgfile = 'examples/message.txt'  # can be any type of file
encfile = 'examples/encoded.png'
msgfile_decoded = 'tmp.txt'

# check max size of message you can embed in vslfile
bpcs.capacity(vslfile, alpha)
# embed msgfile in vslfile, write to encfile
# bpcs.encode(vslfile, msgfile, encfile, alpha)
# bpcs.decode(encfile, msgfile_decoded, alpha) # recover message from encfile
