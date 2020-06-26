#include <iostream>
#include <string>

#include "MoveSets.h"

#define BOARD_SIZE 8

const int pawn = 100;
const int bishop = 305;
const int knight = 300;
const int rook = 500;
const int queen = 900;
const int king = 2000;


int board[BOARD_SIZE][BOARD_SIZE];
const int startup[8][8] = { rook, knight, bishop, queen, king, bishop, knight, rook, pawn, pawn,pawn,pawn,pawn,pawn,pawn, pawn, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -pawn, -pawn, -pawn, -pawn, -pawn, -pawn, -pawn, -pawn, -rook, -knight, -bishop, -queen, -king, -bishop, -knight, -rook};
bool running = true;

void clearBoard()
{
	for(int y = 0; y < BOARD_SIZE; y++)
	{
		for(int x = 0; x < BOARD_SIZE; x++)
		{
			board[x][y] = startup[y][x];
		}
	}
};

std::string getInput()
{
	std::string ret;
	std::cin >> ret;
	return ret;
}

void printHelp()
{
	std::cout << "help    |  Prints the help page." << std::endl;
	std::cout << "print   |  Prints the board." << std::endl;
	std::cout << "restart |  Restarts the chess game." << std::endl;
	std::cout << "quit    |  Quits the program." << std::endl;
	std::cout << std::endl;
}

void printPiece(int piece)
{
	std::string p;
	
	switch(piece)
	{
		case rook:
			p = "♖";
			break;
		case bishop:
			p = "♗";
			break;
		case knight:
			p = "♘";
			break;
		case king:
			p = "♔";
			break;
		case queen:
			p = "♕";
			break;
		case pawn:
			p = "♙";
			break;
		case -rook:
			p = "♜";
			break;
		case -bishop:
			p = "♝";
			break;
		case -knight:
			p = "♞";
			break;
		case -king:
			p = "♚";
			break;
		case -queen:
			p = "♛";
			break;
		case -pawn:
			p = "♟";
			break;
		case 0:
			p = "☐";
			break;
		default:
			p = "☐";
			break;
	};
	
	std::cout << p;
}

void printBoard()
{
	std::cout << " ";
	for(int x = 0; x < BOARD_SIZE; x++)
	{
		std::cout << " " << x+1;
	}
	std::cout << "\n";
	
	for(int y = 0; y < BOARD_SIZE; y++)
	{
		std::cout << char(65+y);
		for(int x = 0; x < BOARD_SIZE; x++)
		{
			std::cout << " ";
			printPiece(board[x][y]);
		}
		std::cout << std::endl;
	}
	std::cout << std::endl;
};

std::string toLowerCase(std::string str)
{
	std::string ret;
	for(int i = 0; i < str.length(); i++)
	{
		if(int(str[i]) >= 65 && int(str[i]) <= 90)
		{
			ret.push_back(str[i] + 32);
		}
		else
		{
			ret.push_back(str[i]);
		}
	}
	return ret;
}

int setPieceAt(int a, int b, int piece)
{
	board[b][a] = piece;
}

int getPieceAt(int a, int b)
{
	return board[b][a];
}

int biggest(int a, int b)
{
	if(a > b)
		return a;
	
	return b;
}

void interpretMove(int a, int b, int c, int d)
{
	int piece = getPieceAt(a, b);
	
	if(piece == 0)
	{
		std::cout << "No Piece Located There." << std::endl;
		return;
	}
	
	MoveSet moveSet = getMoveSetFromPiece(piece);
	
	if(moveSet.constant)
	{
		Vec2 ratio = Vec2(c - a, d - b);
		
		float x = ratio.x / biggest(ratio.x, ratio.y);
		float y = ratio.y / biggest(ratio.x, ratio.y);
		
		std::cout << x << ", " << y << std::endl;
		
		for(int i = 0; i < moveSet.attacks.size(); i++)
		{
			Vec2 attack = moveSet.attacks[i];
			if(attack.x == x && attack.y == y)
			{
				std::cout << "Valid Move." << std::endl;
				return;
			}
		}
		std::cout << "Invalid Move." << std::endl;
	}
	else
	{
		if(moveSet.passable)
		{
			
		}
		else
		{
			
		}
	}
}

void processInput(std::string input)
{
	std::cout << std::endl;
	
	if(input.substr(0, 4) == "quit")
	{
		running = false;
	}
	else if(input.substr(0, 4) == "help")
	{
		printHelp();
	}
	else if(input.substr(0, 7) == "restart")
	{
		clearBoard();
		printBoard();
	}
	else if(input.substr(0, 5) == "print")
	{
		printBoard();
	}
	else
	{
		if(input.length() != 4)
		{
			std::cout << "Invalid Move / Command.\n\n";
			return;
		}
		
		int a = (int)toLowerCase(input.substr(0, 1))[0];
		int b = (int)toLowerCase(input.substr(1, 1))[0];
		int c = (int)toLowerCase(input.substr(2, 1))[0];
		int d = (int)toLowerCase(input.substr(3, 1))[0];
		
		if(a >= 97 && a <= 104 && c >= 97 && c <= 104 && b >= 49 && b <= 56 && d >= 49 && d <= 56)
		{
			interpretMove(a - 97, b - 49, c - 97, d - 49);
		}
		else
		{
			std::cout << "Invalid Move / Command.\n\n";
		}
	}
}

int main() 
{
	setupMoveSets();
	clearBoard();
	printHelp();
	printBoard();
	
	while(running)
	{
		processInput(getInput());
	}
	
	return 0;
};