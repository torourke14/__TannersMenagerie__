// Tanner O'Rourke
// Spring 2017 CSCI 2270 Data Structures
// Final Project - Hash Tables

#include "hashTable.h"

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

// ---------------Constructor-----------------------------------------------------//
hashTable::hashTable(int arrSize) {
    tableSize = arrSize;
    addrCollisions = 0;
    addrSearchOps = 0;
    chainCollisions = 0;
    chainSearchOps = 0;

    dataChaining = new player*[arrSize];
    dataAddressing = new player*[arrSize];
    for (int i = 0; i < tableSize; i++) { // set all indices to NULL
        dataChaining[i] = NULL;
        dataAddressing[i] = NULL;
    }
}

// ------------------------print info------------------------------------------//

void hashTable::printInfo() {
    cout<<"===== Hash Table Results====="<<endl;
    cout<<"Array Size: "<<tableSize<<endl;
    cout<<"Collisions using Open Addressing: "<<addrCollisions<<endl;
    cout<<"Search Operations using Open Addressing: "<<addrSearchOps<<endl;
    cout<<"Collisions using Chaining: "<<chainCollisions<<endl;
    cout<<"Search operations using chaining: "<<chainSearchOps<<endl;
    cout<<endl;
}

// -----------------------table creation------------------------------//

int hashTable::hashSum(string key, int tableSize) {
    int seed = 1;
    unsigned int hash = seed;
    for (int x = 0; x < key.length(); x++) {
        hash = hash * 101 + key[x];
    }
    //sum = sum % tableSize;
    return hash % tableSize;
}

void hashTable::addTableChaining(player* newPlayer) {
    // using dataChaining array
    // colliding key values are added to end of singly linked list

    int i = hashSum(newPlayer -> cName, tableSize);
    if (dataChaining[i] == NULL) { // if new player
        dataChaining[i] = newPlayer;
        dataChaining[i]->next = NULL;
    } else { // have to chain, find spot

        player* temp = dataChaining[i];
        bool duplicate = false;
        if (temp -> playerID == newPlayer -> playerID && !duplicate) { // duplicate of first index, add ONLY new team
                duplicate = true;
                team temp;
                temp.yearID = newPlayer->playerTeams[0].yearID;
                temp.teamID = newPlayer->playerTeams[0].teamID;
                temp.leagueID = newPlayer->playerTeams[0].leagueID;
                temp.salary = newPlayer->playerTeams[0].salary;
                dataAddressing[i]->playerTeams.push_back(temp);
            }
        while (temp -> next != NULL  && !duplicate) {
            if (temp -> playerID == newPlayer -> playerID && !duplicate) { // duplicate player case, add ONLY new team
                duplicate = true;
                team temp;
                temp.yearID = newPlayer->playerTeams[0].yearID;
                temp.teamID = newPlayer->playerTeams[0].teamID;
                temp.leagueID = newPlayer->playerTeams[0].leagueID;
                temp.salary = newPlayer->playerTeams[0].salary;
                dataAddressing[i]->playerTeams.push_back(temp);
                return;
            }
            temp = temp -> next;
            chainSearchOps++; /*--------------------------*/
        }
        chainSearchOps++; /*------------------------------*/

        if (!duplicate) { // if duplicate not found at hash index
            chainCollisions++; /*-----------------------------*/
            dataChaining[i] -> next = newPlayer;
            newPlayer -> next = NULL;
        }

    }

}

void hashTable::addTableAddr(player* newPlayer) {
    // using dataAddressing array
    // colliding key values are stored in array itself at different index

    int i = hashSum(newPlayer -> cName, tableSize);
    if (dataAddressing[i] == NULL) { // if new player
        dataAddressing[i] = newPlayer;
    } else { // index to new spot OR add duplicate
        int orgI = i;
        i++;
        bool foundDup = false;
        while (dataAddressing[i] != NULL) { // search up array
            if (dataAddressing[i]->playerID == newPlayer->playerID & !foundDup) { // duplicate case
                foundDup = true;
                team temp;
                temp.yearID = newPlayer->playerTeams[0].yearID;
                temp.teamID = newPlayer->playerTeams[0].teamID;
                temp.leagueID = newPlayer->playerTeams[0].leagueID;
                temp.salary = newPlayer->playerTeams[0].salary;
                dataAddressing[i]->playerTeams.push_back(temp);
                return;
            }
            if (i == tableSize) { // if gets to end, starts looping from beginning
                i = 0;
            }
            if (i == orgI) { // if array is full and can't find a spot, leave
                return;
            }
            i++;
            addrSearchOps++; /*-------------------*/
        }

        if (!foundDup) { // not duplicate, add to new spot
            addrCollisions++; /*-------------*/
            dataAddressing[i] = newPlayer;
        }
    }

}

// ---------------------------Find player-------------------------------------------------------//

void hashTable::findPlayer(string first, string last) {
    int addrFindSearchOps = 0;
    int chainFindSearchOps = 0;
    string playerName = first + last;
    cout<<"=====Search Results====="<<endl;

    // ----------------chaining search--------------
    int i = hashSum(playerName, tableSize);
    player* temp = dataAddressing[i];
    bool foundC = false;
    while (temp != NULL && !foundC) {
        chainFindSearchOps++; /*--------------*/
        if (temp -> cName == playerName && !foundC) {
            foundC = true;
            cout<<"Search Operations using Chaining: "<<addrFindSearchOps<<endl;
            cout<<endl;
            cout<< "First name: "<<temp->firstName <<endl;
            cout<< "Last name: "<<temp->lastName <<endl;
            cout<< "Birth year: "<<temp->birthYear <<endl;
            cout<< "Birth Country: "<<temp->birthCountry <<endl;
            cout<< "Weight: "<<temp->weight <<endl;
            cout<< "Height: "<<temp->height <<endl;
            cout<< "Bats: "<<temp->bats <<endl;
            cout<< "Throws: "<<temp->throws <<endl;
            cout<< "Teams and Salary: " <<endl;
            cout<<temp->playerTeams.size()<<endl;
            for (int i = 0; i < temp->playerTeams.size(); i++) { // loop through all teams
                cout<< temp->playerTeams[i].yearID <<",";
                cout<< temp->playerTeams[i].teamID <<",";
                cout<< temp->playerTeams[i].leagueID <<",";
                cout<< temp->playerTeams[i].salary <<endl;
            }
            break;
        }
        temp = temp -> next;
    } // end of chaining search while loop
    if (!foundC) {
        cout<<"Player not found."<<endl;
    }


    //----------open addressing search-----------------//
    bool foundOA = false;
    for (int i = 0; i < tableSize; i++) {

        addrFindSearchOps++; /*------------------*/
        if (dataAddressing[i] == NULL) {
            // if index not filled do nothing
        } else if (dataAddressing[i]->cName == playerName && !foundOA) {
            foundOA = true;
            cout<<endl;
            cout<<"Search operations using Open Addressing: "<<chainFindSearchOps<<endl;
            cout<<endl;
            cout<<"First name: "<<dataAddressing[i]->firstName<<endl;
            cout<<"Last name: "<<dataAddressing[i]->lastName<<endl;
            cout<<"Birth year: "<<dataAddressing[i]->birthYear<<endl;
            cout<<"Birth Country: "<<dataAddressing[i]->birthCountry<<endl;
            cout<<"Weight: "<<dataAddressing[i]->weight<<endl;
            cout<<"Height: "<<dataAddressing[i]->height<<endl;
            cout<<"Bats: "<<dataAddressing[i]->bats<<endl;
            cout<<"Throws: "<<dataAddressing[i]->throws<<endl;
            cout<<"Teams and Salary: "<<endl;
            cout<<dataAddressing[i]->playerTeams.size()<<endl;
            for (int x = 0; x < dataAddressing[i]->playerTeams.size(); x++) { // loop through all teams
                cout<<dataAddressing[i]->playerTeams[x].yearID<<",";
                cout<<dataAddressing[i]->playerTeams[x].teamID<<",";
                cout<<dataAddressing[i]->playerTeams[x].leagueID<<",";
                cout<<dataAddressing[i]->playerTeams[x].salary<<endl;
            }
            break;
        }
    } // end of OA for loop
    if (!foundOA) {
        cout<<"Player not found."<<endl;
    }
    cout<<endl;
}

// -----------------------------Deconstructor---------------------------------------------//
hashTable::~hashTable() {

}

