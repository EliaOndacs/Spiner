from source import *
import sys,os

class TextEditor:
    def __init__(self, filename):
        self.text = []
        self.cursor_y = 0
        self.cursor_x = 0
        self.line_num = 1
        self.load_file(filename)

    def load_file(self, filename):
        with open(filename, 'r') as f:
            self.text = [line.strip() for line in f.readlines()]

    def run(self):
        while True:
            self.draw_screen()
            command = input('> ')
            if command == 'q':  # exit
                break
            elif command == '':  # save
                self.save_file()
            elif command.startswith('up'):  # move cursor up
                self.cursor_y = max(0, self.cursor_y - 1)
            elif command.startswith('down'):  # move cursor down
                self.cursor_y = min(len(self.text) - 1, self.cursor_y + 1)
            elif command == '':  # insert new line
                self.text.insert(self.cursor_y, '')
                self.cursor_y += 1
                self.cursor_x = 0
            else:  # insert character
                if self.cursor_y < len(self.text):
                    self.text[self.cursor_y] += command
                    self.cursor_x += len(command)
                else:
                    self.text.append(command)
                    self.cursor_y += 1
                    self.cursor_x = len(command)

    def draw_screen(self):
        print('\n' * 20)  # clear screen
        for i, line in enumerate(self.text):
            print(f'{i + 1}: {line}')
        print(f'{self.line_num}: ', end='')
        if self.cursor_y < len(self.text):
            print(self.text[self.cursor_y][:self.cursor_x], end='')
            print(' ' ,(len(self.text[self.cursor_y]) - self.cursor_x), end='')
        print()

    def save_file(self):
        with open(sys.argv[-1], 'w') as f:
            f.write('\n'.join(self.text))

editor = TextEditor(sys.argv[-1])  # load example.txt by default
editor.run()
