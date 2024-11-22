import re
import subprocess


def objdump_search(binary, search_terms):
    cmd = ["objdump", "-S", binary, "-M", "intel"]
    output = subprocess.check_output(cmd, universal_newlines=True)

    addresses = []
    pattern = re.compile(r"^\s*([0-9a-f]+):")
    for line in output.splitlines():
        if all(term.lower() in line.lower() for term in search_terms):
            match = pattern.search(line)
            if match:
                addresses.append(int(match.group(1), 16))
    return addresses
