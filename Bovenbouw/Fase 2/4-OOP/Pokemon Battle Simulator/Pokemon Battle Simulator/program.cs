using Pokemons;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Trainers;

namespace Pokemon_Battle_Simulator
{
    internal class program
    {   
        static private void SWrite(string text, int ms, bool newLine = true)
        {   
            if(newLine)
            {
                Console.WriteLine(text);
            }
            else
            {
                Console.Write(text);
            }
            Thread.Sleep(ms);
        }

        static void Main(string[] args)
        {
            Console.Write("Press any key to continue");
            Console.ReadKey(true); Console.WriteLine();

            SWrite("Welcome player 1!", 400);
            SWrite("What is your name? >>", 500, false);
            string player1Name = Console.ReadLine() + "";
            Trainer player1 = new Trainer(player1Name);

            SWrite("Welcome player 2!", 400);
            SWrite("What is your name? >>", 500, false);
            string player2Name = Console.ReadLine() + "";
            Trainer player2 = new Trainer(player2Name);

            Console.WriteLine();
            SWrite($"{player1.getName()} throws its pokemon into the field!", 1000);
            player1.Throw(0);

            Console.WriteLine();
            SWrite($"{player2.getName()} throws its pokemon into the field!", 1000);
            player2.Throw(0);
        }
    }
}
