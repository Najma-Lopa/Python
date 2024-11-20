def all_type(first, *args, **kargs):
    print (first)
    for word in args :
        print(word)
    for nam,value in kargs.items():
     print(nam,value)
all_type("naaa","ami","pai","hello",name="najma", last="lopa")
