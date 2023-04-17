using System;

namespace Pokemons
{

    class Pokemon
    {
        private string name;
        private string strength;
        private string weakness;

        public Pokemon(string name, string strength, string weakness)
        {
            this.name = name;
            this.strength = strength;
            this.weakness = weakness; 
        }
        public string GetName()
        {
            return name;
        }
        public void Battlecry(string cry)
        {
            Console.WriteLine($"{cry}!");
        }
    }
}