// Tanner O'Rourke
// Spring 2017 CSCI 2270 Data Structures
// Final Project - Hash Tables
// final Project main

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include "hashTable.h"

using namespace std;

void printMenu() {
    cout<<"======Main Menu======"<<endl;
    cout<<"1. Query Hash Table"<<endl;
    cout<<"2. Quit Program"<<endl;
}

int main (int argc, char*argv[]) {
    char* fileName = argv[1];
    int tableSize = atoi(argv[2]);
    hashTable a(tableSize);

    ifstream fileIn;
	fileIn.open(fileName);

    string line;
    bool first = false;
    while (getline(fileIn, line)) { // loops over every line in file
        if (!first) {
            first = true;
        } else {
            stringstream ss(line);

            string strYearID; /* real value int */ // year playing
            int yearID;
            string teamID;
            string leagueID; // Either AL or NL
            string pID; //string ID for the player
            string strSalary; /* real value int */
            int salary;
            string first; // first name
            string last; // last name
            string strBirthYear; /* real value int */
            int birthYear;
            string birthCountry;
            string strwt; /* real value int */ // players weight
            int wt;
            string strht; /* real value int */ // player’s	height
            int ht;
            string batsLeft; // how the player bats, either right (R) or left (L) handed, or switch
            string throwsLeft;
            getline(ss, strYearID, ',');
            getline(ss, teamID, ',');
            getline(ss, leagueID, ',');
            getline(ss, pID, ',');
            getline(ss, strSalary, ',');
            getline(ss, first, ',');
            getline(ss, last, ',');
            getline(ss, strBirthYear, ',');
            getline(ss, birthCountry, ',');
            getline(ss, strwt, ',');
            getline(ss, strht, ',');
            getline(ss, batsLeft, ',');
            getline(ss, throwsLeft);
            //int handling
            yearID = atoi(strYearID.c_str());
            salary = atoi(strSalary.c_str());
            birthYear = atoi(strBirthYear.c_str());
            wt = atoi(strwt.c_str());
            ht = atoi(strht.c_str());
            player *newPlayer = new player(first,last,pID,birthYear,birthCountry,wt,ht,batsLeft, throwsLeft, yearID, leagueID, teamID, salary);
            a.addTableChaining(newPlayer);
            player *newPlayer2 = new player(first,last,pID,birthYear,birthCountry,wt,ht,batsLeft, throwsLeft, yearID, leagueID, teamID, salary);
            a.addTableAddr(newPlayer2);

        } // end of else
    } // end of while

    a.printInfo();

    string input;
    while(input != "2") {
        printMenu();
        cin>>input;

        if (input == "1") { // 1 | find Player
            string first;
            string last;

            cout<<"Enter the player's first name: "<<endl;
            cin.ignore();
            getline(cin, first);
            cout<<"Enter the player's last name: "<<endl;
            getline(cin, last);

            a.findPlayer(first, last);
        } else if (input == "2") { // 2 | Quit
            cout<<"Goodbye!"<<endl;
        }
    }
    return 0;
}

