using System;

namespace Pokemons
{

    class Charmender : Pokemon
    {
        private string name = "";

        public Charmender(string name) :base(name, "fire", "water")
        {
            this.name = name;
        }

        public override void Battlecry(string cry)
        {
            Console.WriteLine($"{name}: '{cry}!'");
        }
    }
}