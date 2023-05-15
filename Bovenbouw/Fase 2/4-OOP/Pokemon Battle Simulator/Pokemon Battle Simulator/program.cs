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
            while (true) {
                SWrite("Welcome player 1!", 400);
                SWrite("What is your name? >>", 500, false);
                string player1Name = Console.ReadLine() + "";
                Trainer player1 = new Trainer(player1Name);

                SWrite("Welcome player 2!", 400);
                SWrite("What is your name? >>", 500, false);
                string player2Name = Console.ReadLine() + "";
                Trainer player2 = new Trainer(player2Name);

                for (int i = 0; i < 6; i++)
                {
                    Console.WriteLine();
                    SWrite($"{player1.getName()} throws its pokemon into the field!", 1000);
                    player1.Throw(i);
                    player1.getActivePokemon().Battlecry(player1.getActivePokemon().GetName());
                    Thread.Sleep(3000);


                    Console.WriteLine();
                    SWrite($"{player2.getName()} throws its pokemon into the field!", 1000);
                    player2.Throw(i);
                    player2.getActivePokemon().Battlecry(player2.getActivePokemon().GetName());
                    Thread.Sleep(3000);

                    SWrite("", 1000);
                    player1.Return();
                    Thread.Sleep(1000);

                    SWrite("", 1000);
                    player2.Return();
                    Thread.Sleep(1000);
                }
                Console.WriteLine("Do you want to restart? Y/N");
                string retry = "" + Console.ReadLine();
                if(retry == "y")
                {
                    continue;
                }
                else
                {
                    Console.WriteLine("I assume you mean no");
                    Environment.Exit(0);
                }
            }
        }
    }
}
