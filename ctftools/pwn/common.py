from pwn import *

# split horizontally
context.terminal = ["tmux", "splitw", "-h"]


def connect(exe, host, port):
    context.binary = exe.path
    if args.GDB:
        gdbscript = """
            break *main
            continue
        """
        return gdb.debug(exe.path, gdbscript)
    elif args.REMOTE:
        return remote(host, port)
    else:
        return process(exe.path)
