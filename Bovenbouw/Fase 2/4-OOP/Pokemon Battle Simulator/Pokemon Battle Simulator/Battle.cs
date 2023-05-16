using Pokemons;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Trainers;

namespace Pokemon_Battle_Simulator
{
    class Battle
    {
        Trainer trainer1 = new Trainer("");
        Trainer trainer2 = new Trainer("");

        public Battle(Trainer trainer1, Trainer trainer2)
        {
            this.trainer1 = trainer1;
            this.trainer2 = trainer2;
        }
        public void Start()
        {
            Random rng = new Random();
            bool finished = false;
            List<int> t1DefeatedPokemons = new List<int>;
            while(!finished)
            {
                int randIndex = rng.Next(5);
                trainer1.Throw(randIndex);
                Pokemon t1ActivePokemon = trainer1.getActivePokemon();
                t1ActivePokemon.Battlecry(t1ActivePokemon.GetName());

                randIndex = rng.Next(5);
                trainer2.Throw(randIndex);
                Pokemon t2ActivePokemon = trainer2.getActivePokemon();
                t1ActivePokemon.Battlecry(t1ActivePokemon.GetName());
                Console.WriteLine();

                Utils.SlowWrite($"{t1ActivePokemon.GetName()} uses its {t1ActivePokemon.GetStrength()} attack!");
                Utils.SlowWrite($"{t2ActivePokemon.GetName()} uses its {t2ActivePokemon.GetStrength()} attack!");
                Console.WriteLine();

                string p1Weakness = t1ActivePokemon.getWeakness();
                string p1Strength = t1ActivePokemon.GetStrength();

                string p2weakness = t2ActivePokemon.getWeakness();
                string p2Strength = t2ActivePokemon.GetStrength();

                bool t1Win = false;
                bool t2Win = false;
                if (p1Strength == p2weakness)
                {
                    t1Win = true;
                }   
                if(p2Strength == p1Weakness)
                {
                    t2Win = true;
                }

                if(t1Win == t2Win)
                {
                    Utils.SlowWrite("The battle has concluded into a draw!");
                }
                else if (t1Win)
                {
                    Utils.SlowWrite($"{trainer1.getName()} their {t1ActivePokemon.getSubClass()} has won the battle!");
                }
                else if (t2Win)
                {
                    Utils.SlowWrite($"{trainer2.getName()} their {t2ActivePokemon.getSubClass()} has won the battle!");
                }
            }
        }
    }
}
