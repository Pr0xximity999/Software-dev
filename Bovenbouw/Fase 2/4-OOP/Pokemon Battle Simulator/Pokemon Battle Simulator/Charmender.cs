using Pokemon_Battle_Simulator;
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
        public override string getSubClass()
        {
            return "Charmender";
        }

        public override void Battlecry(string cry)
        {
            Utils.SlowWrite($"{name}:", newLine: false);
            Utils.SlowWrite($"'{cry}!'");
        }
    }
}