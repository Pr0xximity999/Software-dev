using Pokeballs;
using Pokemons;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Trainers
{
    internal class Trainer
    {
        private int currPokemon = -1;
        private string name;
        private List<Pokeball> belt = new List<Pokeball>() 
        { 
            new Pokeball(new Pokemon("Charmender", "Fire", "Water")),
            new Pokeball(new Pokemon("Charmender", "Fire", "Water")),
            new Pokeball(new Pokemon("Charmender", "Fire", "Water")),
            new Pokeball(new Pokemon("Charmender", "Fire", "Water")),
            new Pokeball(new Pokemon("Charmender", "Fire", "Water")),
            new Pokeball(new Pokemon("Charmender", "Fire", "Water")),
        };
        public Trainer(string name)
        {
            this.name = name;
        }

        public string getName()
        {
            return name;
        }
        public void Throw(int index)
        {   
            if(index == currPokemon)
            {
                Console.WriteLine("This pokemon is already in the field");
            }
            else if(currPokemon != -1)
            {
                this.Return();
            }

            if(belt[index].Open())
            {
                Console.WriteLine($"{name}: '{belt[index].GetName()} I choose you!'");
                belt[index].GetPokemon().Battlecry(belt[index].GetName());
                currPokemon = index;
            }
        }
        public void Return()
        {
            if (belt[currPokemon].Close())
            {
                Console.WriteLine($"{name}: '{belt[currPokemon].GetName()}, come back!'");
            }
        }
    }
}
