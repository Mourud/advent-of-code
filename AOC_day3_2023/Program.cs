using System.Diagnostics.Contracts;
using Microsoft.VisualBasic;

String[] input = File.ReadAllLines("example.txt");
bool select = false;
int retval = 0;
for (int i = 0; i < input.Length; i++)
{

    for (int j = input[i].Length - 1; j >= 0; j--)
    {
        int totalNumber = 0;
        int indexSetPoint = j;

        while (input[i][j] >= '0' && input[i][j] <= '9')
        {

            int digitValue = input[i][j] - '0';
            int digitMultiplier = indexSetPoint - j;
            totalNumber += digitValue * (int)Math.Pow(10, digitMultiplier);
            if (!select)
            {
                if (isNearSymbol(i, j))
                {
                    select = true;
                }
            }
            if (j == 0)
                break;
            j--;

        }
        if (select == true)
        {
            retval += totalNumber;
            select = false;
        }

    }
}

Console.WriteLine(retval);
bool isNearSymbol(int x, int y)
{
    
    if((y-1) >                                              `0 ){
        
    }
    if((y+1) < input[x].Length){
        
    }
    if((x-1) >0 ){
        
    }
    if((x+1) < input.Length){
        
    }
    if(input[y-1] != null)
    bool down = is ValidSymbol(input[x][y - 1]);
    bool up = isValidSymbol(input[x][y + 1]);
    bool left = isValidSymbol(input[x - 1][y]);
    bool right = isValidSymbol(input[x + 1][y]);
    bool downleft = isValidSymbol(input[x - 1][y - 1]);
    bool upright = isValidSymbol(input[x + 1][y + 1]);
    bool upleft = isValidSymbol(input[x - 1][y + 1]);
    bool downright = isValidSymbol(input[x + 1][y - 1]);
    return (down || up || left || right || downleft || upright || upleft || downright);
}

bool isValidSymbol(char symbol)
{
    return ((symbol >= '!' && symbol <= '-') || (symbol >= ':' && symbol <= '@') || (symbol >= '[' && symbol <= '`') || (symbol >= '{' && symbol <= '~') || (symbol == '/'));
}