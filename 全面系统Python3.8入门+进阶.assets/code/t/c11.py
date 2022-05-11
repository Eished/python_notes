'''
This is a c11 doc
'''
infos = dir()
print(infos)

print('变量名：')
print('name:'+__name__)
print('packge:'+(__package__ or 'no packge'))
print('doc:'+__doc__ or 'no doc')
print('file:'+__file__ or 'no file')
