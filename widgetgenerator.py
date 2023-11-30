import tkinter as tk

class ButtonGenerator(tk.Button):
    def __init__(self, root):
        self.root = root
        self.button = None

    def set_text(self, text):
        self.text = text
        return self
    
    def set_command(self, command):
        self.command = command
        return self
    
    def set_width(self, width):
        self.width = width
        return self
    
    def set_bg_color(self, bg_color):
        self.bg_color = bg_color
        return self
    
class ButtonGeneratorGrid(ButtonGenerator):
    def set_pos(self, row, column):
        self.row = row
        self.column = column
        return self
    
    def build(self):
        self.button = tk.Button(self.root, text=self.text, command=self.command, width=self.width, bg=self.bg_color)
        self.button.grid(row=self.row, column=self.column)
        return self.button
    
class ButtonGeneratorPack(ButtonGenerator):
    def set_anchor(self, anchor):
        self.anchor = anchor
        return self
    
    def build(self):
        self.button = tk.Button(self.root, text=self.text, command=self.command, width=self.width, bg=self.bg_color)
        self.button.pack(anchor=self.anchor)
        return self.button

class LabelGenerator(tk.Label):
    def __init__(self, root):
        self.root = root
        self.label = None

    def set_text(self, text):
        self.text = text
        return self
    
    def set_bg_color(self, bg_color):
        self.bg_color = bg_color
        return self
    
class LabelGeneratorGrid(LabelGenerator):
    def set_pos(self, row, column):
        self.row = row
        self.column = column
        return self
    
    def build(self):
        self.label = tk.Label(self.root, text=self.text, bg=self.bg_color)
        self.label.grid(row=self.row, column=self.column)
        return self.label

class LabelGeneratorPack(LabelGenerator):
    def set_anchor(self, anchor):
        self.anchor = anchor
        return self
    
    def build(self):
        self.label = tk.Label(self.root, text=self.text, bg=self.bg_color)
        self.label.pack(anchor=self.anchor)
        return self.label
    
class FrameGenerator(tk.Frame):
    def __init__(self, root):
        self.root = root
        self.frame = None

class FrameGeneratorGrid(FrameGenerator):
    def set_pos(self, row, column):
        self.row = row
        self.column = column
        return self
    
    def build(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=self.row, column=self.column)
        return self.frame
    
class FrameGeneratorPack(FrameGenerator):
    def build(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack()
        return self.frame

class LabelFrameGenerator(tk.LabelFrame):
    def __init__(self, root):
        self.root = root
        self.labelframe = None

    def set_text(self, text):
        self.text = text
        return self

class LabelFrameGeneratorGrid(LabelFrameGenerator):
    def set_pos(self, row, column):
        self.row = row
        self.column = column
        return self

    def build(self):
        self.labelframe = tk.LabelFrame(self.root, text=self.text)
        self.labelframe.grid(row=self.row, column=self.column)
        return self.labelframe
    
class EntryGenerator(tk.Entry):
    def __init__(self, root):
        self.root = root
        self.entry = None

class EntryGeneratorGrid(EntryGenerator):
    def set_pos(self, row, column):
        self.row = row
        self.column = column
        return self
    
    def build(self):
        self.entry = tk.Entry(self.root)
        self.entry.grid(row=self.row, column=self.column)
        return self.entry
    
class EntryGeneratorPack(EntryGenerator):
    def set_anchor(self, anchor):
        self.anchor = anchor
        return self
    
    def build(self):
        self.entry = tk.Entry(self.root)
        self.entry.pack(anchor=self.anchor)
        return self.entry
    
