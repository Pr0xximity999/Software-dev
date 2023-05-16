using Pokemon_Battle_Simulator;
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
        public override string getSubClass()
        {
            return "Squirtle";
        }

        public override void Battlecry(string cry)
        {
            Utils.SlowWrite($"{name}:", newLine:false);
            Utils.SlowWrite($"'{cry}!'");
        }
    }
}