color_dic = {
    "green":92,

}


class Printer:
    def _get_left_str(self,id):
        return f"\033[{id}m"
    
    def _get_right_str(self):
        return f"\033[0m"
    
    def print(self,text,color):
        content = self._get_left_str(color_dic[color]) + text + self._get_right_str()
        print(content)


if __name__ == "__main__":
    printer = Printer()

    printer.print("123","green")