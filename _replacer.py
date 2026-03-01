import os
import msvcrt

search  = input("Text to find         > ")
replace = input("Text to replace with > ")

files = os.listdir()
for fn in files:
  if not fn.endswith(".lang"):
    continue

  with open(fn, "rb+") as f:
    lines = f.read().decode("utf-8").rstrip().replace("\r\n", "\n").split("\n")
    for i, line in enumerate(lines):
      if search in line:
        while True:
          print("\r%3d | %s" % (i, line.replace(search, replace)), end="")
          if (read := msvcrt.getwch()) == '\r':
            lines[i] = line.replace(search, replace)
          elif read != '\x08':
            continue

          break

    new = "\n".join(lines).encode("utf-8")
    new = new.replace(b"\n", b"\r\n") + b"\r\n"

    f.seek(0)
    f.write(new)
    f.truncate(len(new))
