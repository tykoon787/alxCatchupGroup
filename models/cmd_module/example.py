import cmd

class SayHello(cmd.Cmd):
    """
    Class that will contain Hello Method to say hello
    """
    def do_greet(self, line):
        """ 
        Method that says hello
        """
        print("Hello")

    def do_EOF(self, line):
        """
        Method that handles eof
        """
        return True

if __name__ == '__main__':
    SayHello().cmdloop()
