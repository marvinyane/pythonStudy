#! /usr/bin/python

shoplist = ['apple', 'mango', 'banana', 'carrot']

print 'I have', len(shoplist), 'items to purchase.'

print "These items are:"
for item in shoplist:
    print item,

print '\nI also have to buy rice.'
shoplist.append('rice')
print 'MY shoplist is now', shoplist

print 'I will sort my list now'
shoplist.sort()
print "now my shoplist is", shoplist

print 'the first item I will bus is', shoplist[0]
olditem = shoplist[0]
del shoplist[0]

print 'I have bought the', olditem

print 'My shoplist is now', shoplist
