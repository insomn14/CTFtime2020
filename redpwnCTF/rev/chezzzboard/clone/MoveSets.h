#pragma once

#define MOVESET_COUNT 7

#include <vector>


struct Vec2
{
	float x = 0, y = 0;
	
	Vec2(float x, float y)
	{
		this->x = x; this->y = y;
	}
};

struct MoveSet
{
	int value = 0;
	bool passable = false;
	bool constant = false;
	std::vector<Vec2> moves;
	std::vector<Vec2> attacks;
};


MoveSet moveSets[MOVESET_COUNT];

MoveSet getMoveSetFromPiece(int piece)
{
	int pieceVal = piece;
	
	if(abs(piece) != 100)
		pieceVal = abs(piece);
	
	for(int i = 0; i < MOVESET_COUNT; i++)
	{
		if(moveSets[i].value == pieceVal)
		{
			return moveSets[i];
		}
	}
}

void setupMoveSets()
{
	MoveSet blackPawnM;
	MoveSet whitePawnM;
	MoveSet kingM;
	MoveSet queenM;
	MoveSet bishopM;
	MoveSet knightM;
	MoveSet rookM;
	
	blackPawnM.value = -100;
	blackPawnM.moves.push_back(Vec2(0, 1));
	blackPawnM.attacks.push_back(Vec2(1, 1));
	blackPawnM.attacks.push_back(Vec2(-1, 1));
	moveSets[0] = blackPawnM;
	
	whitePawnM.value = 100;
	whitePawnM.moves.push_back(Vec2(0, 1));
	whitePawnM.attacks.push_back(Vec2(1, -1));
	whitePawnM.attacks.push_back(Vec2(-1, -1));
	moveSets[1] = whitePawnM;
	
	kingM.value = 2000;
	kingM.attacks.push_back(Vec2(1, 0));
	kingM.attacks.push_back(Vec2(-1, 0));
	kingM.attacks.push_back(Vec2(0, -1));
	kingM.attacks.push_back(Vec2(0, 1));
	kingM.attacks.push_back(Vec2(1, 1));
	kingM.attacks.push_back(Vec2(1, -1));
	kingM.attacks.push_back(Vec2(-1, -1));
	kingM.attacks.push_back(Vec2(-1, 1));
	moveSets[2] = kingM;
	
	queenM.value = 900;
	queenM.constant = true;
	queenM.attacks.push_back(Vec2(1, 0));
	queenM.attacks.push_back(Vec2(-1, 0));
	queenM.attacks.push_back(Vec2(0, -1));
	queenM.attacks.push_back(Vec2(0, 1));
	queenM.attacks.push_back(Vec2(1, 1));
	queenM.attacks.push_back(Vec2(1, -1));
	queenM.attacks.push_back(Vec2(-1, -1));
	queenM.attacks.push_back(Vec2(-1, 1));
	moveSets[3] = queenM;
	
	bishopM.value = 305;
	bishopM.constant = true;
	bishopM.attacks.push_back(Vec2(1, 1));
	bishopM.attacks.push_back(Vec2(1, -1));
	bishopM.attacks.push_back(Vec2(-1, -1));
	bishopM.attacks.push_back(Vec2(-1, 1));
	moveSets[4] = bishopM;
	
	rookM.value = 500;
	rookM.constant = true;
	rookM.attacks.push_back(Vec2(1, 0));
	rookM.attacks.push_back(Vec2(-1, 0));
	rookM.attacks.push_back(Vec2(0, 1));
	rookM.attacks.push_back(Vec2(0, -1));
	moveSets[5] = rookM;
	
	knightM.value = 300;
	knightM.passable = true;
	knightM.attacks.push_back(Vec2(2, 1));
	knightM.attacks.push_back(Vec2(2, -1));
	knightM.attacks.push_back(Vec2(-2, 1));
	knightM.attacks.push_back(Vec2(-2, -1));
	knightM.attacks.push_back(Vec2(1, 2));
	knightM.attacks.push_back(Vec2(-1, 2));
	knightM.attacks.push_back(Vec2(1, -2));
	knightM.attacks.push_back(Vec2(-1, -2));
	moveSets[6] = knightM;
};








