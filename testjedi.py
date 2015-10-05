import jedi
filename = "main.py"
with open(filename) as f:
    source = f.read()
script = jedi.Script(source, 4, len("foo.Foo"), filename)
print(script.completions())


filename = "bar/baz.py"
with open(filename) as f:
    source = f.read()
script = jedi.Script(source, 5, len("    foo.Foo"), filename)
print(script.completions())
