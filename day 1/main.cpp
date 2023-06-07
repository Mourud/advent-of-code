#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    string line;
    ifstream myfile("input.txt");

    int total = 0;
    int max = 0;
    int flag = 0;
    while (getline(myfile, line))
    {
        try
        {
            int i = std::stoi(line);
            total += i;
        }
        catch (const std::invalid_argument &ia)
        {
            if (flag == 0) {
                max = total;
                flag =1;
            }
            if (total > max){
                max = total;
            }
            total = 0;
            cout << max << endl;
            
        }
        
    }

    return 0;
}