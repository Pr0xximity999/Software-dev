using System;

namespace Pokemons
{

    class Bulbasaur : Pokemon
    {
        private string name = "";

        public Bulbasaur(string name) :base(name, "leaf", "fire")
        {
            this.name = name;
        }

        public override void Battlecry(string cry)
        {
            Console.WriteLine($"{name}: '{cry}!'");
        }
    }
}