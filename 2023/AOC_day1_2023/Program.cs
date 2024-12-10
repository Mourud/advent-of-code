List<String> words = [  "zero",
                        "one", 

                        "two",
                        "three",

                        "four", 
                        "five", 

                        "six", 
                        "seven", 

                        "eight", 

                        "nine"];

string[] lines = File.ReadAllLines(@"input.txt");
Console.WriteLine(lines.Length);
int total = 0;
for (int i = 0; i < lines.Length; i++)
{
    string line = lines[i];
    int j = 0;
    while (line[j] < '0' || line[j] > '9')
    {
        j++;
    }
    int firstDigit = line[j] - '0';
    int lastDigit = firstDigit;
    int firstIndex = j;
    string prestring = line[..j];
    foreach (var word in words)
    {
        int temp = prestring.IndexOf(word);
        if (temp != -1 && temp < firstIndex)
        {
            firstIndex = temp;
            firstDigit = words.IndexOf(word);
        }
        
        int last = line.LastIndexOf(word);
    }
    int lastIndex = j;
    for (; j < line.Length; j++)
    {
        if (line[j] >= '0' && line[j] <= '9')
        {
            lastDigit = line[j] - '0';
            lastIndex = j;
        }
    }
    string poststring = line[lastIndex..];
    int pivot = lastIndex;
    foreach (var word in words)
    {
        int temp = poststring.LastIndexOf(word) + pivot;
        if(temp > lastIndex)
        {
            lastIndex = temp;
            lastDigit = words.IndexOf(word);
        }
    }
    Console.WriteLine("LINE: " + line);
    Console.WriteLine("FIRST DIGIT: " + firstDigit + "   LAST DIGIT: " + lastDigit);

    total += firstDigit * 10 + lastDigit;
}
Console.WriteLine("Answer: " + total);
