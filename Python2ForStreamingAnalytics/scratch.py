GREEN = "\033[92m"
def DisplayTree(self):
    z = self.height - 1
    x = 1
    line = ''
    for i in range(self.height):
        line = line + (' ' * z + self.leaves * x + ' ' * z + '\n')
        x += 2
        z -= 1

        print GREEN + line
    return line