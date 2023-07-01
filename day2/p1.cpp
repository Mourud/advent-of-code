#include <iostream>
#include <string>
#include <fstream>

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
        case 'X':
            // A X (1 + 3)
            // B X (1 + 0)
            // C X (1 + 6)
            total += 1;
            switch (opp_move)
            {
            case 'A':
                total += 3;
                break;
            case 'C':
                total += 6;
                break;
            }
            break;
        case 'Y':
            // A Y (2 + 6)
            // B Y (2 + 3)
            // C Y (2 + 0)
            total += 2;
            switch (opp_move)
            {
            case 'A':
                total += 6;
                break;
            case 'B':
                total += 3;
                break;
            }
            break;
        case 'Z':
            // A Z (3 + 0)
            // B Z (3 + 6)
            // C Z (3 + 3)
            total += 3;
            switch (opp_move)
            {
            case 'B':
                total += 6;
                break;
            case 'C':
                total += 3;
                break;
            }
            break;
        }
    }
    cout << total << endl;
    return 0;
}