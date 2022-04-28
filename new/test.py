class loop:

    def __init__(self,button_list):
        self.run_stack = []
        self.list_loop_buttons = []
        self.button_list = button_list
    def add_loop_in_stack(self):
        self.list_loop_buttons = self.list_loop_buttons[::-1]
        print(self.list_loop_buttons)
        x = self.list_loop_buttons[0].split()
        val = int(x[1])
        print('val of loop:'+ str(val))
        for j in range(val):  
            for i in range(1,len(self.list_loop_buttons)-1):
                self.run_stack.append(self.list_loop_buttons[i])
        self.list_loop_buttons = []        
        
    def exec_run_stack(self):
        count = 0
        for i in range(len(self.run_stack)):
            x = self.run_stack[i].split()
            if x[0] !='LOOP':
                #print("exec")
                count = count + 1
        print(count)

    def add_button_list_in_run_stack(self):
        for i in  range(len(self.button_list)):
            x = self.button_list[i].split()
            print(x)
            if x[0] !='END':
                self.run_stack.append(self.button_list[i])
            else:
                self.list_loop_buttons.append(self.button_list[i])
                while(len(self.list_loop_buttons)!=0):
                    line = self.run_stack.pop()
                    p = line.split()
                    if(p[0]=='LOOP'):
                        self.list_loop_buttons.append(line)
                        self.add_loop_in_stack()
                        break
                    else:
                        self.list_loop_buttons.append(line)
                        continue


if __name__ == "__main__":
    button_list = ['LOOP 5','LOOP 2','LOOP 3','MOVE 10','END 3','END 2','END 5']
    l = loop(button_list)
    l.add_button_list_in_run_stack()
    l.exec_run_stack()






