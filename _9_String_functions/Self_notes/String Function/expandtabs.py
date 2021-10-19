"""*******************expandtabs() ********************"""
print('expandtabs() : : expands tab to mentioned spaces, 8 being default.')
s = 'hello\t world'
print('without expandtabs() :', s)
s1 = s.expandtabs()
print('expandtabs() without mentioning space will take 8 as default  :', s1)
s2 = s.expandtabs(15)
print('expandtabs() with space 5 :', s2)

