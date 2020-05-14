def f():
    global s
    print(s)
    s = "Función"
    print(s)


s = "Global"
f()
print(s)