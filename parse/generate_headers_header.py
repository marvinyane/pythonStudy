#! /usr/bin/python
import sys

def generate_headers_header(fh, filename):
    name = '_'.join(filename.split('.'))
    macro = "__%s__" % (name.upper())

    fh.write("#ifndef %s\n" % (macro))
    fh.write("#define %s\n\n" % (macro))

    fh.write("#ifdef __cplusplus\n")
    fh.write('extern "C" {\n')
    fh.write("#endif\n\n")


def generate_headers_tail(fh):
    fh.write("#ifdef __cplusplus\n")
    fh.write('}\n')
    fh.write("#endif\n\n")

    fh.write("#endif\n")

if __name__ == '__main__':
    generate_headers_header(sys.stdout, "bluetec_general_if.h")
    generate_headers_tail(sys.stdout)
