using Pokeballs;
using Pokemon_Battle_Simulator;
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

        public int getActivePokemonIndex()
        {
            return currPokemon;
        }
        public Pokemon getActivePokemon()
        {
            return belt[currPokemon].GetPokemon();
        }

        public void Throw(int index)
        {
            Pokeballs.Pokeballs indexed_pokemon = belt[index];
            Utils.SlowWrite($"{name}: '{indexed_pokemon.GetName()},",80 ,false);
            Utils.SlowWrite(" I choose you!'", 40);
            currPokemon = index;
        }
        public void Return()
        {
            Utils.SlowWrite($"{name}: '{belt[currPokemon].GetName()},", 80, false);
            Thread.Sleep(100);
            Utils.SlowWrite(" come back!'", 40);
        }
    }
}
