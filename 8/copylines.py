# append lines from one text file to another

def append_lines(src, dst):
  with open(src, "r") as src_file:
    with open(dst, "a") as dst_file:
      for line in src_file:
        dst_file.write(line)