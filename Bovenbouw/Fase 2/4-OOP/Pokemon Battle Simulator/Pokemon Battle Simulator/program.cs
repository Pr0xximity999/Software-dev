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
            Console.WriteLine("Welcome!");
            Thread.Sleep(1000);
            Console.WriteLine("You have a new charmender!");
            Thread.Sleep(1000);
            while (true)
            {
                Console.WriteLine("What do you want to name him/her/they/them/xim/xer/attack chopper/ze/zer?");
                string name = Console.ReadLine();
                if (name == null) { name = ""; }

                if(name != "")
                {
                    Pokemon charmender = new Pokemon(name, "fire", "water");
                    for (int i = 0; i < 11; i++)
                    {
                        charmender.Battlecry(name);
                        Thread.Sleep(100);
                    }

                }
                else
                {
                    Console.WriteLine("Enter a valid name");
                    Thread.Sleep(1000);
                }
            }
        }
    }
}
