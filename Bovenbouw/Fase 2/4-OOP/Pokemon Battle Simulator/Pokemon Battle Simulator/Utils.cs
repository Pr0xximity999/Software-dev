using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pokemon_Battle_Simulator
{
    class Utils
    {
        public static void SleepWrite(string text, int ms, bool newLine = true)
        {
            if (newLine)
            {
                Console.WriteLine(text);
            }
            else
            {
                Console.Write(text);
            }
            Thread.Sleep(ms);
        }

        public static void SlowWrite(string text, int ms=100, bool newLine = true)
        {
            foreach(char letter in text)
            {
                Console.Write(letter);
                Thread.Sleep(ms);
            }
            if(newLine)
            {
                Console.Write("\n");

            }
        }
    }
}
