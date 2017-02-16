import sys, cmd, os

#del __builtins__.__dict__['__import__']
del __builtins__.__dict__['eval']
del __builtins__.__dict__['execfile']
del __builtins__.__dict__['input']

intro = """
Welcome to Secure Python Interpreter 
================================================

Rules:
    -Do not import anything
    -No peeking at files!
    -No sharing of flags :)

"""

 
def execute(command):
       exec(command) in locals()
 
class Jail(cmd.Cmd):
 
    prompt     = '>>> '
 
    def do_EOF(self, line):
        sys.exit()
 
    def emptyline(self):
        return cmd.Cmd.emptyline(self)
 
    def default(self, line):
        sys.stdout.write('\x00')
 
    def postcmd(self, stop, line):
        if any(f in line for f in self.filtered):
            print "Do you think my code is so insecure ?"
        else:
           try:
                execute(line)
           except NameError:
                print "NameError: name '%s' is not defined" % line
           except Exception:
                print "Error: %s" % line
        return cmd.Cmd.postcmd(self, stop, line)
 
if __name__ == "__main__":
    try:
        Jail().cmdloop(intro)
    except KeyboardInterrupt:
        print "\rBye bye !"
 
