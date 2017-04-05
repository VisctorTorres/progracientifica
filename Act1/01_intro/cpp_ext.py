@register_cell_magic
def py(line, cell):
    """Compile, execute C++ code, and return the
    standard output."""
    # We first retrieve the current IPython interpreter instance.
    ip = get_ipython()
    # We define the source and executable filenames.
    source_filename = 'hola_mundo.py'
    program_filename = '_temp'
    # We write the code to the C++ file.
    cell = cell.replace("raw_input","input")
    cell = cell.replace("print ","print(")
    cell = cell.replace(".\"",".\")")
    with open(source_filename, 'w') as f:
        f.write(cell)
    # We compile the C++ code into an executable.
    compile = ip.getoutput("python2 {0:s}".format(
              source_filename))
    # We execute the executable and return the output.
    output = ip.getoutput('python3 {0:s}'.format(source_filename))
    print('\n'.join(output))
    #%run ./hola_mundo.py

def load_ipython_extension(ipython):
       """This function is called when the extension is loaded.
       It accepts an IPython InteractiveShell instance.
       We can register the magic with the `register_magic_function`
       method of the shell instance."""
       ipython.register_magic_function(cpp, 'cell')