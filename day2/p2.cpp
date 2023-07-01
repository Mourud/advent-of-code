#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    string line;

    ifstream myfile("input.txt");
    int total = 0;

    while (getline(myfile, line))
    {
        char opp_move = line[0];
        char ind_move = line[2];

        switch (ind_move)
        {
        case 'X': // you lose
                  // A X 0 + 3
                  // B X 0 + 1
                  // C X 0 + 2
            switch (opp_move)
            {
            case 'A':
                total += 3;
                break;
            case 'B':
                total += 1;
                break;
            case 'C':
                total += 2;
                break;
            }
            break;
        case 'Y': // you draw
                  // A Y 3 + 1
                  // B Y 3 + 2
                  // C Y 3 + 3
            total += 3;
            switch (opp_move)
            {
            case 'A':
                total += 1;
                break;
            case 'B':
                total += 2;
                break;
            case 'C':
                total += 3;
                break;
            }
            break;
        case 'Z': // you win
                  // A Z 6 + 2
                  // B Z 6 + 3
                  // C Z 6 + 1
            total += 6;
            switch (opp_move)
            {
            case 'A':
                total += 2;
                break;
            case 'B':
                total += 3;
                break;
            case 'C':
                total += 1;
                break;
            }
            break;
        }
    }
    cout << total << endl;
    return 0;
}