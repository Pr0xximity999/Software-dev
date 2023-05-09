using Pokemons;
using System;

namespace Pokeballs
{

    class Pokeballs
    {
        private Pokemon pokemon;
        private bool isFull;
        
        public Pokeballs()
        {
            this.isFull = false;
        }
        public Pokeballs(Pokemon pokemon)
        {
            this.pokemon = pokemon;
            this.isFull = true;
        }

        public string GetName()
        {   
            if(isFull)
            { 
                return pokemon.GetName();
            }
            else
            {
                return "";
            }
        }
        public bool getState()
        {
            return isFull;
        }
        public Pokemon GetPokemon()
        {
            return pokemon;
        }
    }
}