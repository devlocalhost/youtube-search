import pafy
ask = input('URL// ')

v = pafy.new(ask)
s = v.getbest()

print("Size: %s" % s.get_filesize())
filename = s.download()