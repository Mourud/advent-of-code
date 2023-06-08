#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
    string line;
    ifstream myfile("day 1/input.txt");

    int total = 0;
    int max[3] = {0};
    int flag = 0;
    while (getline(myfile, line))
    {

        if (line.empty())
        {
            if (flag == 0)
            {
                max[0] = total;
                max[1] = total;
                max[2] = total;
                flag = 1;
            }
            else if (total > max[0])
            {
                int temp = max[1];
                max[1] = max[0];
                max[0] = total;
                max[2] = temp;
            }
            else if (total > max[1])
            {
                int temp = max[1];
                max[1] = total;
                max[2] = temp;
            }
            else if (total > max[2])
            {
                max[2] = total;
            }
            total = 0;
        }
        else
        {
            total += stoi(line);
        }
    }
    total = max[0] + max[1] + max[2];
    std::cout << max[0] << endl;
    std::cout << max[1] << endl;
    std::cout << max[2] << endl;
    std::cout << total << endl;

    return 0;
}