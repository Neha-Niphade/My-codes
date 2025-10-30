class Text_Editor:
    def __init__(self):
        self.undo_stack=[]
        self.redo_stack=[]
        
    def make_change(self,text):
        self.undo_stack.append(text)
        self.redo_stack.clear()
        print("Change saved successfully")
        
    def Undo(self):
        if(len(self.undo_stack)>1):
            last_change=self.undo_stack.pop()
            self.redo_stack.append(last_change)
            print("undo done")
        else:
            print("Nothing to undo")
    
    def Redo(self):
        if (len(self.redo_stack)>1):
            redo=self.redo_stack.pop()
            self.undo_stack.append(redo)
            print("redo done")
        else:
            print("nothing to redo")
            
    def Display(self):
        if self.undo_stack:
            print("current doc state: ",self.undo_stack[-1])
        else:
            print("empty")
def Main():
    editor=Text_Editor()
    while(True):
        print("Menu")
        print("1.Make a change\n2.Undo\n3.Redo\n4.Display\n5.Exit")
        ch=int(input("Enter choice:"))
        if ch == 1:
            text = input("Enter new document text: ")
            editor.make_change(text)
        elif ch == 2:
            editor.Undo()
        elif ch == 3:
            editor.Redo()
        elif ch == 4:
            editor.Display()
        elif ch == 5:
            print("👋 Exiting program.")
            break
        else:
            print("❌ Invalid choice, try again.")
if __name__=="__main__":
    Main()
