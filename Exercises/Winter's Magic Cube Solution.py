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

    #Basic init
    def __getitem__(self, key) -> list:
        return [self.front,self.right,self.back,self.left,self.top,self.bottom][key]
    
    def __str__(cl):
        #oneliner :skull:
        return f'      {cl[4][0]:<2} {cl[4][1]:<2}\n      {cl[4][2]:<2} {cl[4][3]:<2}\n{cl[3][0]:<2} {cl[3][1]:<2} {cl[0][0]:<2} {cl[0][1]:<2} {cl[1][0]:<2} {cl[1][1]:<2} {cl[2][0]:<2} {cl[2][1]:<2}\n{cl[3][2]:<2} {cl[3][3]:<2} {cl[0][2]:<2} {cl[0][3]:<2} {cl[1][2]:<2} {cl[1][3]:<2} {cl[2][2]:<2} {cl[2][3]:<2}\n      {cl[5][0]:<2} {cl[5][1]:<2}\n      {cl[5][2]:<2} {cl[5][3]:<2}'

    #Moving
    def move(self, sequence:list[str]|tuple[str], show:bool=True) -> None:
        "Evaluates sequence of moves for the cube and prints each move"
        for i in sequence:
            #I am not doing 12 if statements for each movement
            eval("self.move_"+i.upper().replace("'", '_prime')+"()")
            if show: print("Move: ", i,"\n",self,sep="",flush=True)
            #Flush buffer to ensure printed before next command

    #The following section contains many magic numbers
    #Where do the magic numbers come from? Up my arse!
    #Rotate a cow in 3D in your head and you will see!
    def move_U(s):
        s.top = [s.top[2], s.top[0], s.top[3], s.top[1]]
        s.left[:2], s.front[:2], s.right[:2], s.back[:2] = s.front[:2], s.right[:2], s.back[:2], s.left[:2]

    def move_U_prime(s):
        s.top = [s.top[1], s.top[3], s.top[0], s.top[2]]
        s.left[:2], s.front[:2], s.right[:2], s.back[:2] = s.back[:2], s.left[:2], s.front[:2], s.right[:2]

    def move_D(s):
        s.bottom = [s.bottom[2], s.bottom[0], s.bottom[3], s.bottom[1]]
        s.left[2:], s.front[2:], s.right[2:], s.back[2:] = s.back[2:], s.left[2:], s.front[2:], s.right[2:]

    def move_D_prime(s):
        s.bottom = [s.bottom[1], s.bottom[3], s.bottom[0], s.bottom[2]]
        s.left[2:], s.front[2:], s.right[2:], s.back[2:] = s.front[2:], s.right[2:], s.back[2:], s.left[2:]

    def move_R(s):
        s.right = [s.right[2], s.right[0], s.right[3], s.right[1]]
        s.bottom[1], s.bottom[3], s.front[1], s.front[3], s.top[1], s.top[3], s.back[2], s.back[0] = s.back[2], s.back[0], s.bottom[1], s.bottom[3], s.front[1], s.front[3], s.top[1], s.top[3]

    def move_R_prime(s):
        s.right = [s.right[1], s.right[3], s.right[0], s.right[2]]
        s.bottom[1], s.bottom[3], s.front[1], s.front[3], s.top[1], s.top[3], s.back[2], s.back[0] = s.front[1], s.front[3], s.top[1], s.top[3], s.back[2], s.back[0], s.bottom[1], s.bottom[3]

    def move_L(s):
        s.left = [s.left[2], s.left[0], s.left[3], s.left[1]]
        s.top[0], s.top[2], s.front[0], s.front[2], s.bottom[0], s.bottom[2], s.back[3], s.back[1] = s.back[3], s.back[1], s.top[0], s.top[2], s.front[0], s.front[2], s.bottom[0], s.bottom[2]

    def move_L_prime(s):
        s.left = [s.left[1], s.left[3], s.left[0], s.left[2]]
        s.top[0], s.top[2], s.front[0], s.front[2], s.bottom[0], s.bottom[2], s.back[3], s.back[1] = s.front[0], s.front[2], s.bottom[0], s.bottom[2], s.back[3], s.back[1], s.top[0], s.top[2]

    def move_F(s):
        s.front = [s.front[2], s.front[0], s.front[3], s.front[1]]
        s.top[2], s.top[3], s.right[0], s.right[2], s.bottom[1], s.bottom[0], s.left[3], s.left[1] = s.left[3], s.left[1], s.top[2], s.top[3], s.right[0], s.right[2], s.bottom[1], s.bottom[0]

    def move_F_prime(s):
        s.front = [s.front[1], s.front[3], s.front[0], s.front[2]]
        s.top[2], s.top[3], s.right[0], s.right[2], s.bottom[1], s.bottom[0], s.left[3], s.left[1] = s.right[0], s.right[2], s.bottom[1], s.bottom[0], s.left[3], s.left[1], s.top[2], s.top[3]

    def move_B(s):
        s.back = [s.back[2], s.back[0], s.back[3], s.back[1]]
        s.top[1], s.top[0], s.left[0], s.left[2], s.bottom[2], s.bottom[3], s.right[3], s.right[1] = s.right[3], s.right[1], s.top[1], s.top[0], s.left[0], s.left[2], s.bottom[2], s.bottom[3]

    def move_B_prime(s):
        s.back = [s.back[1], s.back[3], s.back[0], s.back[2]]
        s.top[1], s.top[0], s.left[0], s.left[2], s.bottom[2], s.bottom[3], s.right[3], s.right[1] = s.left[0], s.left[2], s.bottom[2], s.bottom[3], s.right[3], s.right[1], s.top[1], s.top[0]

    #End of magic number wizardry, end of class

#Main code
scrambled_cube = Cube_2x2()
from random import choices
from re import compile, findall
scrambled_cube.move(choices(["U","U'","D","D'","L","L'","R","R'","F","F'","B","B'"],k=15),show=False)
print("Scrambled cube:\n", scrambled_cube,flush=True)
solved_cube = Cube_2x2()
pattern = compile(r"[udlrfbUDLRFB]'?")
while scrambled_cube[:] != solved_cube[:]:
    try:
        scrambled_cube.move(findall(pattern=pattern, string=input("Enter move(s): ")))
    except SyntaxError:
        print("Invalid move, try again")
print("TADAA DONE")