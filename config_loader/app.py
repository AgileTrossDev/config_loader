from foo import foo
from foo import config

print(dir(foo))

print ("START")

conf = config.Config("SCOTT",1.1,3)


a = foo.create_foo(conf)
a.disp()

print ("EXIT")
