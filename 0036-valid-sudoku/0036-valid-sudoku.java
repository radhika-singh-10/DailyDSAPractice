class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<Character>[] rows = new HashSet[9];
        Set<Character>[] cols = new HashSet[9];
        Set<Character>[] squares = new HashSet[9];
        for (int r = 0; r < 9; r++) {
            rows[r] = new HashSet<Character>();
            cols[r] = new HashSet<Character>();
            squares[r] = new HashSet<Character>();
        }
        for (int r=0;r<9;r++){
            for (int c=0;c<9;c++){
                if (board[r][c]=='.'){
                    continue;
                }
                if (rows[r].contains(board[r][c])){
                    return false;
                }
                rows[r].add(board[r][c]);
                if (cols[c].contains(board[r][c])){
                    return false;
                }
                cols[c].add(board[r][c]);
                if (squares[(r/3)*3+c/3].contains(board[r][c])){
                    return false;
                }
                squares[(r/3)*3+c/3].add(board[r][c]);
            }
        }
        return true;









        //boolean status=true;
        // for(int i=0;i<6;i+=3){
        //     List<Character> tn=new ArrayList();
        //     for(int j=0;j<6;j+=3){
        //         if(tn.get(board[i][j])!=-1) tn.add(board[i][j]);
        //         else return false;
        //         if(tn.get(board[i][j+1])!=-1) tn.add(board[i][j+1]);
        //         else return false;
        //         if(tn.get(board[i][j+2])!=-1) tn.add(board[i][j+2]);
        //         else return false;
                
        //         if(tn.get(board[i+1][j])!=-1) tn.add(board[i+1][j]);
        //         else return false;
        //         if(tn.get(board[i+1][j+1])!=-1) tn.add(board[i+1][j+1]);
        //         else return false;
        //         if(tn.get(board[i+1][j+2])!=-1)  tn.add(board[i+1][j+2]);
        //         else return false;

        //         if(tn.get(board[i+2][j])!=-1) tn.add(board[i+2][j]);
        //         else return false;
        //         if(tn.get(board[i+2][j+1])!=-1) tn.add(board[i+2][j+1]);
        //         else return false;
        //         if(tn.get(board[i+2][j+2])!=-1) tn.add(board[i+2][j+2]);
        //         else return false;
        //     }
        // }
        // return true;
    }
}