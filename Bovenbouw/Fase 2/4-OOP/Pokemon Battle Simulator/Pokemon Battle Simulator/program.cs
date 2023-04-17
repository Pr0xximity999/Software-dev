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
        static void Main(string[] args)
        {
            //These steps look written by chatgpt
            //the player "start" the game

            //The player start the game
            Console.WriteLine("Welcome!");
            Thread.Sleep(1000);
            Console.WriteLine("You have a new charmender!");
            Thread.Sleep(1000);
            while (true)
            {   
                //The player gives a name to a charmander
                Console.WriteLine("What do you want to name it?");
                string name = Console.ReadLine();
                if (name == null) { name = ""; }

                if(name != "")
                {
                    Pokemon charmender = new Pokemon(name, "fire", "water");

                    //The carmander does its battlycry for ten times
                    for (int i = 0; i < 11; i++)
                    {
                        charmender.Battlecry(name);
                        Thread.Sleep(100);
                    }
                    //The player can give a new name to the same charmande
                    Console.WriteLine("Would you like to rename it? y/n");
                    string repeat = Console.ReadLine();
                    if(repeat == null) { repeat = ""; }
                    //Repeat previous steps
                    if(repeat == "y")
                    {
                        continue;
                    }
                    //Otherwise exit
                    else
                    {
                        Console.WriteLine("I assume you meant no :)");
                        Thread.Sleep(1000);
                        Environment.Exit(0);
                    }


                }
                else
                {
                    Console.WriteLine("Enter at least a single character!");
                    Thread.Sleep(1000);
                }
            }
        }
    }
}
