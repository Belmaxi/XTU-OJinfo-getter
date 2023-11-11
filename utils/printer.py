class Color():
    RED = 91
    GREEN = 92
    YELLOW = 93
    BLUE = 94
    PURPLE = 95
    CYAN = 96



class Printer:
    @staticmethod
    def _get_left_str(id):
        return f"\033[{id}m"
    
    @staticmethod
    def _get_right_str():
        return f"\033[0m"
    
    @staticmethod
    def print(text,color:int) -> None:
        content = Printer._get_left_str(color) + text + Printer._get_right_str()
        print(content)
    
    @staticmethod
    def console_print_warning(text) -> None:
        Printer.print(text,Color.YELLOW)
    
    @staticmethod
    def console_print_success(text) -> None:
        Printer.print(text,Color.GREEN)
    
    @staticmethod
    def console_print_error(text) -> None:
        Printer.print(text,Color.RED)


if __name__ == "__main__":
    printer = Printer()

    printer.print("123","green")