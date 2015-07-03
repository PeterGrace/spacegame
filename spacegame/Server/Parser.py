'''command parser accepts registered commands, registered functions are found,
   called with appropriate source objects (player, client sock, etc) checked
   for security'''


class Parser(object):
    def __init__(self):
        pass

    def register_cmd(self, cmd, method, min_lvl=0, **kwargs):
        '''Register a command with this instance of the parser.

        Positional Arguments:
        cmd      -- base cmd name (string)
        method   -- function/method that is called (callable)
        min_lvl  -- minimum level this command requires (default 0)
        **kwargs -- passed into called function as args
        '''
        pass

    def parse(self, data, src, **kwargs):
        '''Parse a raw string

        Position Arguments:
        data     -- raw string to parse
        src      -- source of the raw string (Player, etc)
        **kwargs -- additional arguments that are forwarded to the command
        '''
        pass
