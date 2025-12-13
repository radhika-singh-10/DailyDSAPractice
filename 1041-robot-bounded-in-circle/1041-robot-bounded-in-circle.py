class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        #initial pt-0,0

        #no movement
        if not instructions:
            return True

        n=len(instructions)

        #coordinate maintainence
        x_coor, y_coor = 0, 0
        d='N'
        #circle -> come back to the same coordinate

        #logic for position
        #if d==n: l->w, r->e
        #if d==s: l->e, r->w
        #if d==e: l->n, r->s
        #if d==w: l->s, r->n
        
        def changePositions(d, turn):
            if d == 'N':
                return 'W' if turn == 'L' else 'E'
            elif d == 'S':
                return 'E' if turn == 'L' else 'W'
            elif d == 'E':
                return 'N' if turn == 'L' else 'S'
            else: 
                return 'S' if turn == 'L' else 'N'


        def getDirections(d):
            if d=='N':
                return [0,1]
            elif d=='S':
                return [0,-1]
            elif d=='E':
                return [1,0]
            else:
                return [-1,0]

        for i in instructions:
            if i == 'G':
                x, y = getDirections(d)
                x_coor += x
                y_coor += y
            elif i == 'L' or i == 'R':
                d = changePositions(d, i)

        return (x_coor == 0 and y_coor == 0) or d != 'N'
                

                
                


