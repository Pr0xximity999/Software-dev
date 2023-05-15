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
        private List<Pokeballs.Pokeballs> belt = new List<Pokeballs.Pokeballs>() 
        { 
            new Pokeballs.Pokeballs(new Bulbasaur("Bulbasaur1")),
            new Pokeballs.Pokeballs(new Bulbasaur("Bulbasaur2")),
            new Pokeballs.Pokeballs(new Charmender("Charmender1")),
            new Pokeballs.Pokeballs(new Charmender("Charmender2")),
            new Pokeballs.Pokeballs(new Squirtle("squirtle1")),
            new Pokeballs.Pokeballs(new Squirtle("squirtle2")),
        };
        public Trainer(string name)
        {
            this.name = name;
        }

        public string getName()
        {
            return name;
        }

        public Pokemon getActivePokemon()
        {
            return belt[currPokemon].GetPokemon();
        }

        public void Throw(int index)
        {
            Pokeballs.Pokeballs indexed_pokemon = belt[index];
            Console.WriteLine($"{name}: '{indexed_pokemon.GetName()} I choose you!'");
            currPokemon = index;
        }
        public void Return()
        {
            Console.WriteLine($"{name}: '{belt[currPokemon].GetName()}, come back!'");
        }
    }
}
