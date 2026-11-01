class TextEditor:
    def __init__(self):
        self.current_document_state = ""
        self.undo_stack = []
        self.redo_stack = []

    def make_change(self, new_content):
        self.undo_stack.append(self.current_document_state)
        self.current_document_state = new_content
        self.redo_stack = []
        self.display_document_state()

    def undo_action(self):
        if self.undo_stack:
            self.redo_stack.append(self.current_document_state)
            self.current_document_state = self.undo_stack.pop()
            self.display_document_state()
        else:
            print("Nothing to undo.")

    def redo_action(self):
        if self.redo_stack:
            self.undo_stack.append(self.current_document_state)
            self.current_document_state = self.redo_stack.pop()
            self.display_document_state()
        else:
            print("Nothing to redo.")

    def display_document_state(self):
        print(f"Current Document: '{self.current_document_state}'")


editor = TextEditor()

editor.make_change("Hello")
editor.make_change("Hello World")
editor.undo_action()
editor.make_change("Hello Python")
editor.undo_action()
editor.redo_action()
