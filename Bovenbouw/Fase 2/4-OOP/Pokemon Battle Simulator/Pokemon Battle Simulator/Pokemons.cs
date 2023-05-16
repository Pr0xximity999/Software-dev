using System;

namespace Pokemons
{

    abstract class Pokemon
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
        public string GetStrength()
        {
            return strength;
        }
        public string getWeakness()
        {
            return weakness;
        }
        public abstract string getSubClass();
        public abstract void Battlecry(string cry);
    }
}