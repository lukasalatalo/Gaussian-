package javareview;
import java.util.concurrent.ThreadLocalRandom;
import java.util.Scanner; 
public class PartC {
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		int[][] grid = new int[10][10];
		String [][] sampleGrid = new String[10][10];
		int[] randomRow = new int[10];
		int[] randomCol = new int[10];
		
		Scanner userInput = new Scanner(System.in);
		System.out.println("What is your name?\n");
		String name = userInput.nextLine();
		
		System.out.println(name + ", would you like to play Mine Sweeper?(yes=1, no=2)\n");
		int playGame = userInput.nextInt();
		
		while (playGame!= 1 && playGame != 2) { //ensures that user inputs correctly
			System.out.println("Wrong input. intput 1 or 2?\n");
			playGame = userInput.nextInt();
			
		}
		
		while (playGame == 1) {
			for (int i=0;i<grid.length;i++) {
				while (grid[randomRow[i]][randomCol[i]] == 1) {   //assigns a random value where mines are found in grid
					randomRow[i] = ThreadLocalRandom.current().nextInt(0, 10); 
					randomCol[i] = ThreadLocalRandom.current().nextInt(0,10);
				}
				if (grid[randomRow[i]][randomCol[i]] == 0) {
					randomRow[i] = ThreadLocalRandom.current().nextInt(0, 10);
					randomCol[i] = ThreadLocalRandom.current().nextInt(0,10);
					grid[randomRow[i]][randomCol[i]]=1;
				}
			}
			
			
			System.out.println("Here is the board: \n");
			
			for (int i=0;i<sampleGrid.length;i++) {  //creates a visual representation of the grid
				for (int j=0;j<sampleGrid[i].length;j++) {
					sampleGrid[i][j] = "?";
					System.out.print(sampleGrid[i][j]+", ");
				}
				System.out.println("");
			}
			
			System.out.println("");
			System.out.println("What row would you like to select (1-10)?\n");
			int row = userInput.nextInt();
			System.out.println("What column would you like to select (1-10)?\n");
			int column = userInput.nextInt();
			
			while ((row > 10 || row < 1) || (column>10 || column <1)) { //ensures that user inputs correctly
				System.out.println("Wrong input. What row would you like to select (1-10)?\n");
				row  = userInput.nextInt();
				System.out.println("What column would you like to select (1-10)?\n");
				column = userInput.nextInt();		
			}
			
			
			while (grid[row-1][column-1]!=1) {  //determines if you did not hit a mine
				while (grid[row-1][column-1]==2) { //ensures that user inputs correctly
					System.out.println("You have used this coordinate. Choose another.\n"); 
					System.out.println("What row would you like to select (1-10)?\n");
					row = userInput.nextInt();
					System.out.println("What column would you like to select (1-10)?\n");
					column = userInput.nextInt();
					while ((row > 10 || row < 1) || (column>10 || column <1)) { //ensures that user inputs correctly
						System.out.println("Wrong input. What row would you like to select (1-10)?\n");
						row  = userInput.nextInt();
						System.out.println("What column would you like to select (1-10)?\n");
						column = userInput.nextInt();		
					}
				}
				
				grid[row-1][column-1] = 2;
				sampleGrid[row-1][column-1] = "x";
				
				System.out.println("You've missed a mine! There are " + numMines(grid,row,column) + " mines around this spot.");
				System.out.println("Try Again! \n");
				System.out.println("x on the board marks the places you have been.\n");
				for (int i=0;i<sampleGrid.length;i++) {
					for (int j=0;j<sampleGrid[i].length;j++) {
						System.out.print(sampleGrid[i][j]+", ");
					}
					System.out.println("");
				}
				System.out.println("");
			
				System.out.println("What new row would you like to select (1-10)?\n");
				row = userInput.nextInt();
				System.out.println("What new column would you like to select (1-10)?\n");
				column = userInput.nextInt();
				
				while ((row > 10 || row < 1) || (column>10 || column <1)) { //ensures that user inputs correctly
					System.out.println("Wrong input. What row would you like to select (1-10)?\n");
					row  = userInput.nextInt();
					System.out.println("What column would you like to select (1-10)?\n");
					column = userInput.nextInt();		
				}
				
			}
			
			if (grid[row-1][column-1]==1) {
				System.out.println("You've hit a mine! Game over!\n");
				
			}
			
			System.out.println("");
			System.out.println("Would you like to play again?(yes=1, no=2)\n");
			playGame = userInput.nextInt();
			while (playGame!= 1 && playGame != 2) { //ensures that user inputs correctly
				System.out.println("Wrong input. intput 1 or 2?\n");
				playGame = userInput.nextInt();
				
			}
		}
		
		if (playGame==2) {
			System.out.println("Well, its been fun. Goodbye " + name + ".");
		}
		userInput.close();
	}
	public static int numMines (int [][] grid, int row, int column) {    //finds the number of mines directly beside coordinate
		int sum = 0;
		int c = column-1;
		int r = row-1;
		int count = c+1;
		int count2 = c-1;
		int count3 = r+1;
		int count4 =r-1;
		
		if (count<grid[r].length) {       //checks if there is a mine to the right
			if (grid[r][count] == 1) {
				sum +=1;
			}
		}
		if(count2>=0) {                  //checks if there is a mine to the left
			if(grid[r][count2] ==1) {
				sum+=1;
			}
		}
		if(count3<grid.length) {        //checks if there is a mine above
			if(grid[count3][c] ==1) {
				sum += 1;
			}
		}
		if (count4>=0) {				 //checks if there is a mine below
			if (grid[count4][c]==1) {
				sum+= 1;
			}
		}
		return sum;
		
		
	}
}
