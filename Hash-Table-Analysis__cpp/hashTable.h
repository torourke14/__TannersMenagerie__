// Tanner O'Rourke
// Spring 2017 CSCI 2270 Data Structures
// Final Project - Hash Tables
// hashTable.h

#ifndef HASHTABLE_H
#define HASHTABLE_H

#include <iostream>
#include <vector>
#include <stdlib.h>

using namespace std;

struct team {
    int yearID;
    std::string teamID;
    std::string leagueID;
    int salary;
    /*team (int yrID, std::string tID, std::string lgID, int sal) {
        yearID = yrID;
        teamID = tID;
        leagueID = lgID;
        salary = sal;
    }*/
};

struct player {
    player* next; // used in chaining algorithm
    std::vector<team> playerTeams;

    /*yearID, teamID, leagueID, salary all stored in teams */
    std::string firstName;
    std::string lastName;
    std::string cName;
    std::string playerID; //string ID for the player, used in the Lahman database
    int birthYear;
    std::string birthCountry;
    int weight; // players weight
    int height; // player’s	height
    std::string bats; // either (R) or (L) handed, or switch (S)
    std::string throws;

    player (std::string first,std::string last,std::string pID,int birthY,std::string birthC,int wt,int ht,std::string bL,std::string tL, int yID, std::string tID, std::string lID, int sal) {
            this->firstName = first;
            this->lastName = last;
            this->cName = first + "" + last;
            this->playerID = pID;
            this->birthYear = birthY;
            this->birthCountry = birthC;
            this->weight = wt;
            this->height = ht;
            this->bats = bL;
            this->throws = tL;
            team temp;
            temp.yearID = yID;
            temp.teamID = tID;
            temp.leagueID = lID;
            temp.salary = sal;
            this->playerTeams.push_back(temp);
            next = NULL;
    }
};

class hashTable {
    public:
        hashTable(int); // takes size of array
        ~hashTable();
        void addTableChaining(player*); // creates 'dataChaining' array
        void addTableAddr(player*); // creates 'dataAddressing' array
        int hashSum(std::string, int);
        void printInfo();

        void findPlayer(std::string, std::string); // finds player, displays search data

    protected:
    private:
        int tableSize;
        int addrCollisions;
        int addrSearchOps;
        int chainCollisions;
        int chainSearchOps;
        player **dataChaining;
        player **dataAddressing;
};

#endif // GRAPH_H
