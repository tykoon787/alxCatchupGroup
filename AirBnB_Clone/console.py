import cmd

class HBNBCommand(cmd.Cmd):
    """
    CLI for AirBnB
    """
    prompt = "(hbnb)"
    def do_quit(self, line):
        """
        Exit CLI
        """
        return True

    def do_EOF(self, line):
        """
        Handles EOF, or Exits
        """
        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()