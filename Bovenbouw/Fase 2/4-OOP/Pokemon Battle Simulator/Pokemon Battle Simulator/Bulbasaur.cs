using Pokemon_Battle_Simulator;
using System;

namespace Pokemons
{

    class Bulbasaur : Pokemon
    {
        private string name = "";

        public Bulbasaur(string name) :base(name, "grass", "fire")
        {
            this.name = name;
        }

        public override string getSubClass()
        {
            return "Bulbasaur";
        }

        public override void Battlecry(string cry)
        {
            Utils.SlowWrite($"{name}:",100 ,false);
            Utils.SlowWrite($"'{cry}!'", 50);
        }
    }
}