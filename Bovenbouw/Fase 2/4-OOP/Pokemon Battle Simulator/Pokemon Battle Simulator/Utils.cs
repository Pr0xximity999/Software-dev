using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Input;

namespace Pokemon_Battle_Simulator
{
    class Utils
    {
        static private int multiplier = 1;
        public static void setSpeedMulitplier(int mult)
        {
            multiplier = mult;
        }
        public static void SlowWrite(string text, int ms=50, bool newLine = true, bool waitAtEnd=true)
        {
            ms /= multiplier;
            foreach(char letter in text)
            {
                Console.Write(letter);
                Thread.Sleep(ms);
            }
            if(newLine)
            {
                Console.Write("\n");
                
            }
            if (waitAtEnd)
            {
                Thread.Sleep(ms * 5);
            }
        }
    }
}
