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
        /// <summary>
        /// Print de gegeven text per letter met de gegeven delay
        /// </summary>
        /// <param name="text">De text die geprint word</param>
        /// <param name="ms">De delay tussen iedere letter</param>
        /// <param name="newLine">Bepaald of hij een nieuwe lijn begin aan het eind van de zin</param>
        /// <param name="waitAtEnd">Bepaald of hij wacht aan het eind van de zin(5 keer de delay van ms)</param>
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
