using Pokemons;
using System;

namespace Pokeballs
{

    class Pokeball
    {
        private Pokemon pokemon;
        private bool isEmpty;
        private bool isOpen = false;
        
        public Pokeball()
        {
            this.isEmpty = true;
        }
        public Pokeball(Pokemon pokemon)
        {
            this.pokemon = pokemon;
            this.isEmpty = false;
        }

        public string GetName()
        {   
            if(!isEmpty)
            { 
                return pokemon.GetName();
            }
            else
            {
                return "";
            }
        }
        public Pokemon GetPokemon()
        {
            return pokemon;
        }
        public bool contain(Pokemon pokemon)
        {
             if(isEmpty)
             {
                this.pokemon = pokemon;
                isEmpty = false;
                return true;
             }
            else 
            {
                Console.WriteLine("There is already a pokemon in this ball!");
                return false;
            }
        }
        public bool Open()
        {
            if(!isEmpty && !isOpen)
            {
                isOpen = true;
                return true;
            }
            else if(isEmpty)
            {
                Console.WriteLine("This pokeball is empty");
                return false;
            }
            else
            {
                Console.WriteLine("This pokeball is already opened!");
                return false;
            }
        }
        public bool Close()
        {
            if(isOpen && !isEmpty)
            {
                return true;
            }
            else if (!isOpen)
            {
                Console.WriteLine($"{GetName()} is already in this pokeball!");
                return false;
            }
            else
            {
                Console.WriteLine("This pokeball has no pokemon bound to it!");
                return false;
            }
        }
    }
}