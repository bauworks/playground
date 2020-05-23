# -*- coding: utf-8 -*-
 
a="Hello"
b="world"
 
#文字の連結
c=a+b
print( "%s+%s=%s" % ( a,b,c ) )
 
#文字列の繰り返し
f="a"*10 print( f )
 
#フォーマット文字列で整形
d=format( '%s %s' % (a,b) )
print( d )
 
#置換
g=b.replace('or','OR')
print( g )
 
#文字列両端のスペース、タブ文字、改行を削除
h=' hello \n\n\n'
print( h )
i=h.strip()
print( i )