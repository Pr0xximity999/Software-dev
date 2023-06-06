using Pokemons;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Trainers;

namespace Pokemon_Battle_Simulator
{
    static class Battle
    {

        private static int roundsPlayed = 0;
        private static int battlesPlayed = 0;
        private static int lastRoundWon = 2;

        public static void Start(Trainer trainer1, Trainer trainer2)
        {   
            //Increases the battle count
            battlesPlayed++;
            roundsPlayed = 0;

            //Initialized the trainers and pokemon lists
            List<Trainer> trainers = new List<Trainer>()
            {
                trainer1,
                trainer2
            };
            Random rng1 = new Random();
            Random rng2 = new Random();
            List<List<int>> DefeatedPokemons = new List<List<int>>
            {
                new List<int> { },
                new List<int> { }
            };

            //Go on untill the battle is finished
            bool finished = false;
            while (!finished)
            {
                //Checks if one of the trainers is out of pokemons to use
                if (DefeatedPokemons[0].Count == 6)
                {
                    Console.WriteLine();
                    Utils.SlowWrite($"{trainer1.getName()} has lost the battle and is now gay!");
                    Utils.SlowWrite($"{trainer2.getName()} has won the battle!");
                    finished = true;
                    continue;
                }
                if (DefeatedPokemons[1].Count == 6)
                {
                    Utils.SlowWrite($"{trainer2.getName()} has lost the battle and is now gay!");
                    Utils.SlowWrite($"{trainer1.getName()} has won the battle!");
                    finished = true;
                    continue;
                }

                //Displays the correct round number
                roundsPlayed++;
                Console.Clear();
                Console.WriteLine($"BATTLE #{battlesPlayed}");

                //Displays how many pokemons each player has left
                Utils.SlowWrite($"{trainer1.getName()} has {6 - DefeatedPokemons[0].Count} pokemons left");
                Utils.SlowWrite($"{trainer2.getName()} has {6 - DefeatedPokemons[1].Count} pokemons left");

                Console.WriteLine("\n\n");
                Utils.SlowWrite($"ROUND #{roundsPlayed}", 100);
                Console.WriteLine("\n");

                //Chooses player 1 pokemon
                int randIndex1;
                while (true)
                {
                    randIndex1 = rng1.Next(6);
                    if (!DefeatedPokemons[0].Contains(randIndex1))
                    {
                        break;
                    }
                }
                trainers[0].Throw(randIndex1);
                Pokemon t1ActivePokemon = trainers[0].getActivePokemon();
                t1ActivePokemon.Battlecry(t1ActivePokemon.GetName());
                Console.WriteLine();

                //Choose player 2 pokemon
                int randIndex2;
                while (true)
                {
                    randIndex2 = rng2.Next(6);
                    if (!DefeatedPokemons[1].Contains(randIndex2))
                    {
                        break;
                    }
                }
                trainers[1].Throw(randIndex2);
                Pokemon t2ActivePokemon = trainers[1].getActivePokemon();
                t2ActivePokemon.Battlecry(t2ActivePokemon.GetName());
                Console.WriteLine("\n");


                //The battle between pokemons
                Utils.SlowWrite($"{t1ActivePokemon.GetName()} uses its {t1ActivePokemon.GetStrength()} attack!");
                Utils.SlowWrite($"{t2ActivePokemon.GetName()} uses its {t2ActivePokemon.GetStrength()} attack!");
                Console.WriteLine();

                //Checks who won
                bool t1Win = false;
                bool t2Win = false;
                if (t1ActivePokemon.isWeakTo(t2ActivePokemon))
                {
                    t2Win = true;
                }
                if (t2ActivePokemon.isWeakTo(t1ActivePokemon))
                {
                    t1Win = true;
                }

                //If its a draw
                if(t1Win == t2Win)
                {
                    Utils.SlowWrite("The battle has concluded into a draw!");
                    if(lastRoundWon != 2)
                    {
                        lastRoundWon = 0 - lastRoundWon; 
                        DefeatedPokemons[lastRoundWon].Add(trainers[lastRoundWon].getActivePokemonIndex());
                        trainers[lastRoundWon].Return();
                    }
                    else
                    {
                        trainers[0].Return();
                        DefeatedPokemons[0].Add(randIndex1);
                        trainers[1].Return();
                        DefeatedPokemons[1].Add(randIndex2);
                    }

                }

                //If player 1 wins
                else if (t1Win)
                {
                    Utils.SlowWrite($"{trainers[0].getName()} their {t1ActivePokemon.getSubClass()} has won the battle!");
                    DefeatedPokemons[1].Add(randIndex1);
                    trainers[1].Return();
                    lastRoundWon = 0;
                    continue;
                }

                //If player 2 wins
                else if (t2Win)
                {
                    Utils.SlowWrite($"{trainers[1].getName()} their {t2ActivePokemon.getSubClass()} has won the battle!");
                    DefeatedPokemons[0].Add(randIndex1);
                    trainers[0].Return();
                    lastRoundWon = 1;
                    continue;
                }
            }
        }
    }
}
