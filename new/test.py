class loop:

    def __init__(self,button_list):
        self.run_stack = []
        self.list_loop_buttons = []
        self.button_list = button_list
        self.if_list = []
        self.else_list = []
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
        #for i in range(len(self.run_stack)):
        i = 0 
        while(i<len(self.run_stack)):
            x = self.run_stack[i].split()
            print(x)
            count = count + 1
            if x[0]=='IF':
                if x[1]=='FALSE':
                    i = int(x[2])
                    print(i)
                elif x[1]=='TRUE':
                     print("exec")        
            i +=1        

        print(count)

    def assign_if_else_in_run_stack(self):
        for i in range(len(self.run_stack)):
            x = self.run_stack[i].split()
            #print(x)
            if x[0]=='IF':
                self.if_list.append(i)
            elif x[0]=='ENDIF':
                self.run_stack[self.if_list.pop()] += ' ' + str(i)
            elif x[0]=='ELSE':
                self.else_list.append(i)
            elif x[0]=='ENDELSE':
                self.run_stack[self.else_list.pop()]+= ' ' + str(i)        


    def add_button_list_in_run_stack(self):
        for i in  range(len(self.button_list)):
            x = self.button_list[i].split()
            #print(x)
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
    button_list = ['LOOP 2','IF FALSE','MOVE 10','MOVE 10','ENDIF','END 2']
    l = loop(button_list)
    l.add_button_list_in_run_stack()
    l.assign_if_else_in_run_stack()
    l.exec_run_stack()






