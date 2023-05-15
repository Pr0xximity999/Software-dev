using System;

namespace Pokemons
{

    class Squirtle : Pokemon
    {
        private string name = "";

        public Squirtle(string name) :base(name, "water", "leaf")
        {
            this.name = name;
        }
        public override void Battlecry(string cry)
        {
            Console.WriteLine($"{name}: '{cry}!'");
        }
    }
}