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
        static void Main(string[] args)
        {
            while (true) {
                Utils.SlowWrite("Welcome player 1!", 100);
                Utils.SlowWrite("What is your name? >>", 500, false);
                string player1Name = Console.ReadLine() + "";
                Trainer player1 = new Trainer(player1Name);

                Utils.SlowWrite("Welcome player 2!", 400);
                Utils.SlowWrite("What is your name? >>", 500, false);
                string player2Name = Console.ReadLine() + "";
                Trainer player2 = new Trainer(player2Name);

                for (int i = 0; i < 6; i++)
                {
                    Console.WriteLine();
                    Utils.SleepWrite($"{player1.getName()} throws its pokemon into the field!", 1000);
                    player1.Throw(i);
                    player1.getActivePokemon().Battlecry(player1.getActivePokemon().GetName());
                    Thread.Sleep(3000);


                    Console.WriteLine();
                    Utils.SleepWrite($"{player2.getName()} throws its pokemon into the field!", 1000);
                    player2.Throw(i);
                    player2.getActivePokemon().Battlecry(player2.getActivePokemon().GetName());
                    Thread.Sleep(3000);

                    Utils.SleepWrite("", 1000);
                    player1.Return();
                    Thread.Sleep(1000);

                    Utils.SleepWrite("", 1000);
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
