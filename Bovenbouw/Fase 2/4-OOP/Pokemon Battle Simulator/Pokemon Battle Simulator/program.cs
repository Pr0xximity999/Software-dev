using Pokemons;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Pokemon_Battle_Simulator
{
    internal class program
    {   
        static private void SWrite(string text, int ms)
        {
            Console.WriteLine(text);
            Thread.Sleep(ms);
        }

        static void Main(string[] args)
        {
            SWrite("Welcome!", 400);
            SWrite("You have a new charmender!", 1000);
            while (true)
            {   
                SWrite("What do you want to name it?", 10);
                string name = "" + Console.ReadLine();

                if(name != "")
                {
                    Pokemon charmender = new Pokemon(name, "fire", "water");

                    for (int i = 0; i < 11; i++)
                    {
                        charmender.Battlecry(name);
                        Thread.Sleep(100);
                    }
                    SWrite("Would you like to rename it? y/n", 300);
                    string repeat = "" + Console.ReadLine();
                    if(repeat == "y")
                    {
                        continue;
                    }
                    else
                    {
                        SWrite("I assume you meant no :)", 500);
                        Environment.Exit(0);
                    }


                }
                else
                {
                    SWrite("Enter at least a single character!", 800);
                }
            }
        }
    }
}
