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
            Utils.setSpeedMulitplier(3);
            while (true) 
            {
                Utils.SlowWrite("Welcome player 1!");
                Utils.SlowWrite("What is your name? >>", newLine: false);
                string player1Name = Console.ReadLine() + "";
                Trainer player1 = new Trainer(player1Name);

                Utils.SlowWrite("Welcome player 2!");
                Utils.SlowWrite("What is your name? >>", newLine: false);
                string player2Name = Console.ReadLine() + "";
                Trainer player2 = new Trainer(player2Name);

                Battle.Start(player1, player2);
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
