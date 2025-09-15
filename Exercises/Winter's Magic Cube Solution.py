from random import choices
from re import compile, findall

class Cube_2x2():
    "Creates a class of a 2x2 Rubic's Cube"

    #Values for cube printing, uses ASCII escape chars to colour text
    r = "\033[41m"       + '  ' + '\033[0m'
    b = "\033[44m"       + '  ' + '\033[0m'
    o = "\033[48;5;215m" + '  ' + '\033[0m'
    g = "\033[42m"       + '  ' + '\033[0m'
    y = "\033[43m"       + '  ' + '\033[0m'
    w = "\033[47m"       + '  ' + '\033[0m'

    def __init__(self):
        r, b, o, g, y, w = self.r, self.b, self.o, self.g, self.y, self.w
        self.front  = [r, r, r, r]
        self.right  = [b, b, b, b]
        self.back   = [o, o, o, o]
        self.left   = [g, g, g, g]
        self.top    = [y, y, y, y]
        self.bottom = [w, w, w, w]
    def __getitem__(self, key) -> list:
        return [self.front,self.right,self.back,self.left,self.top,self.bottom][key]
    def __str__(self):
        #oneliner cos no one looking at it anyway
        return f'      {self[4][0]:<2} {self[4][1]:<2}\n      {self[4][2]:<2} {self[4][3]:<2}\n{self[3][0]:<2} {self[3][1]:<2} {self[0][0]:<2} {self[0][1]:<2} {self[1][0]:<2} {self[1][1]:<2} {self[2][0]:<2} {self[2][1]:<2}\n{self[3][2]:<2} {self[3][3]:<2} {self[0][2]:<2} {self[0][3]:<2} {self[1][2]:<2} {self[1][3]:<2} {self[2][2]:<2} {self[2][3]:<2}\n      {self[5][0]:<2} {self[5][1]:<2}\n      {self[5][2]:<2} {self[5][3]:<2}' #peekaboo

    #Moving
    def move(self, sequence:list[str]|tuple[str], show:bool=True) -> None:
        "Evaluates sequence of moves for the cube and prints each move"
        for i in sequence:
            #I am not doing 12 if statements for each movement
            #I can probbly structure it but too much effort
            move = i.upper().replace("'", '_prime')
            if move not in ['U', 'D', 'L', 'R', 'F', 'B', 
                "U_prime", "D_prime", "L_prime", "R_prime", "F_prime", "B_prime"]:
                raise NotImplementedError(f"Invalid move '{i}'")
            eval(f"self.move_{move}()")
            if show: print("Move: ", move,"\n",self,sep="",flush=True)
            #Flush buffer to ensure printed before next command

    #The following section contains many magic numbers
    #Where do the magic numbers come from? Up my arse!
    def move_U(self):
        self.top = [self.top[2], self.top[0], self.top[3], self.top[1]]
        self.left[:2], self.front[:2], self.right[:2], self.back[:2] = self.front[:2], self.right[:2], self.back[:2], self.left[:2]
    def move_U_prime(self):
        self.top = [self.top[1], self.top[3], self.top[0], self.top[2]]
        self.left[:2], self.front[:2], self.right[:2], self.back[:2] = self.back[:2], self.left[:2], self.front[:2], self.right[:2]
    def move_D(self):
        self.bottom = [self.bottom[2], self.bottom[0], self.bottom[3], self.bottom[1]]
        self.left[2:], self.front[2:], self.right[2:], self.back[2:] = self.back[2:], self.left[2:], self.front[2:], self.right[2:]
    def move_D_prime(self):
        self.bottom = [self.bottom[1], self.bottom[3], self.bottom[0], self.bottom[2]]
        self.left[2:], self.front[2:], self.right[2:], self.back[2:] = self.front[2:], self.right[2:], self.back[2:], self.left[2:]
    def move_R(self):
        self.right = [self.right[2], self.right[0], self.right[3], self.right[1]]
        self.bottom[1], self.bottom[3], self.front[1], self.front[3], self.top[1], self.top[3], self.back[2], self.back[0] = self.back[2], self.back[0], self.bottom[1], self.bottom[3], self.front[1], self.front[3], self.top[1], self.top[3]
    def move_R_prime(self):
        self.right = [self.right[1], self.right[3], self.right[0], self.right[2]]
        self.bottom[1], self.bottom[3], self.front[1], self.front[3], self.top[1], self.top[3], self.back[2], self.back[0] = self.front[1], self.front[3], self.top[1], self.top[3], self.back[2], self.back[0], self.bottom[1], self.bottom[3]
    def move_L(self):
        self.left = [self.left[2], self.left[0], self.left[3], self.left[1]]
        self.top[0], self.top[2], self.front[0], self.front[2], self.bottom[0], self.bottom[2], self.back[3], self.back[1] = self.back[3], self.back[1], self.top[0], self.top[2], self.front[0], self.front[2], self.bottom[0], self.bottom[2]
    def move_L_prime(self):
        self.left = [self.left[1], self.left[3], self.left[0], self.left[2]]
        self.top[0], self.top[2], self.front[0], self.front[2], self.bottom[0], self.bottom[2], self.back[3], self.back[1] = self.front[0], self.front[2], self.bottom[0], self.bottom[2], self.back[3], self.back[1], self.top[0], self.top[2]
    def move_F(self):
        self.front = [self.front[2], self.front[0], self.front[3], self.front[1]]
        self.top[2], self.top[3], self.right[0], self.right[2], self.bottom[1], self.bottom[0], self.left[3], self.left[1] = self.left[3], self.left[1], self.top[2], self.top[3], self.right[0], self.right[2], self.bottom[1], self.bottom[0]
    def move_F_prime(self):
        self.front = [self.front[1], self.front[3], self.front[0], self.front[2]]
        self.top[2], self.top[3], self.right[0], self.right[2], self.bottom[1], self.bottom[0], self.left[3], self.left[1] = self.right[0], self.right[2], self.bottom[1], self.bottom[0], self.left[3], self.left[1], self.top[2], self.top[3]
    def move_B(self):
        self.back = [self.back[2], self.back[0], self.back[3], self.back[1]]
        self.top[1], self.top[0], self.left[0], self.left[2], self.bottom[2], self.bottom[3], self.right[3], self.right[1] = self.right[3], self.right[1], self.top[1], self.top[0], self.left[0], self.left[2], self.bottom[2], self.bottom[3]
    def move_B_prime(self):
        self.back = [self.back[1], self.back[3], self.back[0], self.back[2]]
        self.top[1], self.top[0], self.left[0], self.left[2], self.bottom[2], self.bottom[3], self.right[3], self.right[1] = self.left[0], self.left[2], self.bottom[2], self.bottom[3], self.right[3], self.right[1], self.top[1], self.top[0] #wow same length

#Main code
scrambled_cube = Cube_2x2()
scrambled_cube.move(choices(["U","U'","D","D'","L","L'","R","R'","F","F'","B","B'"],k=15),show=False)
print("Scrambled cube:", scrambled_cube,flush=True, sep='\n')
solved_cube = Cube_2x2()
pattern = compile(r"[udlrfbUDLRFB]'?")
while scrambled_cube[:] != solved_cube[:]:
    try:
        scrambled_cube.move(
            findall(pattern=pattern, string=input("Enter move(s): "))
            )
    except SyntaxError:
        print("Invalid move, try again")
    except KeyboardInterrupt:
        #unoriginal idea
        print("OPYTHAT", flush=True)
        break
print("TADAA DONE")