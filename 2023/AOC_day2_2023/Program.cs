// Read file input.txt
using System.Data;
using System.Text.RegularExpressions;

string[] lines = File.ReadAllLines("input.txt");

int retVal = 0;
int select = 3;

foreach (string line in lines)
{
    int[] marbles = { 0, 0, 0 };
    string[] gameString = line.Split(":");
    string info = gameString[1];
    for (int i = info.Length - 1; i >= 0; i--)
    {

        if (info[i] == 'e')
        { // blue
            select = 0;
            i -= 5;

        }
        else if (info[i] == 'd')
        { // red
            i -= 4;
            select = 1;

        }
        else if (info[i] == 'n')
        { // green
            i -= 6;
            select = 2;
        }
        int indexSetPoint = i;
        int totalNumber = 0;
        while (info[i] >= '0' && info[i] <= '9')
        {
            int digitValue = info[i] - '0';
            int digitMultiplier = indexSetPoint - i;
            totalNumber += digitValue * (int)Math.Pow(10, digitMultiplier);
            i--;
        }
        if (totalNumber > marbles[select])
            marbles[select] = totalNumber;

    }
// if (marbles[0] <= 14 && marbles[1] <= 12 && marbles[2] <= 13)
//     {
//         string gameNumber = Regex.Match(gameString[0], @"\d+").Value;
//         Int32.TryParse(gameNumber, out int gameNum);
//         retVal += gameNum;
//     }
        Console.WriteLine("BLUE: " + marbles[0] + "   RED: " + marbles[1] + "   GREEN: " + marbles[2]);
        retVal += marbles[0]*marbles[1]*marbles[2];
}
Console.WriteLine(retVal);