//Game data
var games = [
    {
        "title": "Counter-Strike: Global Offensive",
        "price": 0.00,
        "genre": "FPS",
        "rating": 4
    },
    {
        "title": "Dota 2",
        "price": 0.00,
        "genre": "MOBA",
        "rating": 3
    },
    {
        "title": "Goose Goose Duck",
        "price": 4.99,
        "genre": "Action",
        "rating": 2
    },
    {
        "title": "Apex Legends",
        "price": 0.00,
        "genre": "FPS",
        "rating": 4
    },
    {
        "title": "PUBG: BATTLEGROUNDS",
        "price": 29.99,
        "genre": "FPS",
        "rating": 5
    },
    {
        "title": "Lost Ark",
        "price": 49.99,
        "genre": "Action",
        "rating": 1
    },
    {
        "title": "Grand Theft Auto V",
        "price": 29.99,
        "genre": "FPS",
        "rating": 3
    },
    {
        "title": "Call of Duty®: Modern Warfare® II | Warzone™ 2.0",
        "price": 19.99,
        "genre": "FPS",
        "rating": 3
    },
    {
        "title": "Team Fortress 2",
        "price": 0.00,
        "genre": "FPS",
        "rating": 5
    },
    {
        "title": "Rust",
        "price": 39.99,
        "genre": "Action",
        "rating": 5
    },
    {
        "title": "Unturned",
        "price": 0.00,
        "genre": "RPG",
        "rating": 1
    },
    {
        "title": "ELDEN RING",
        "price": 59.99,
        "genre": "RPG",
        "rating": 5
    },
    {
        "title": "ARK: Survival Evolved",
        "price": 10.00,
        "genre": "RPG",
        "rating": 1
    },
    {
        "title": "War Thunder",
        "price": 0.00,
        "genre": "Simulation",
        "rating": 2
    },
    {
        "title": "Sid Meier's Civilization VI",
        "price": 29.99,
        "genre": "Simulation",
        "rating": 3
    },
    {
        "title": "Football Manager 2023",
        "price": 59.99,
        "genre": "Simulation",
        "rating": 3
    },
    {
        "title": "Warframe",
        "price": 0.00,
        "genre": "Looter-shooter",
        "rating": 3
    },
    {
        "title": "EA SPORTS™ FIFA 23",
        "price": 59.99,
        "genre": "Sport",
        "rating": 1
    },
    {
        "title": "Destiny 2",
        "price": 0.00,
        "genre": "FPS",
        "rating": 5
    },
    {
        "title": "Red Dead Redemption 2",
        "price": 59.99,
        "genre": "RPG",
        "rating": 4
    },
    {
        "title": "Tom Clancy's Rainbow Six Siege",
        "price": 19.99,
        "genre": "Simulation",
        "rating": 3
    },
    {
        "title": "The Witcher 3: Wild Hunt",
        "price": 39.99,
        "genre": "RPG",
        "rating": 4
    },
    {
        "title": "Terraria",
        "price": 9.99,
        "genre": "Sandbox",
        "rating": 2
    },
    {
        "title": "Stardew Valley",
        "price": 14.99,
        "genre": "Sandbox",
        "rating": 1
    },
    {
        "title": "Left 4 Dead 2",
        "price": 9.99,
        "genre": "FPS",
        "rating": 4
    },
    {
        "title": "Don't Starve Together",
        "price": 5.09,
        "genre": "RPG",
        "rating": 3
    },
    {
        "title": "MIR4",
        "price": 19.99,
        "genre": "RPG",
        "rating": 3
    },
    {
        "title": "PAYDAY 2",
        "price": 9.99,
        "genre": "Action",
        "rating": 2
    },
    {
        "title": "Path of Exile",
        "price": 0.00,
        "genre": "RPG",
        "rating": 4
    },
    {
        "title": "Project Zomboid",
        "price": 14.99,
        "genre": "Simulation",
        "rating": 4
    },
    {
        "title": "Valheim",
        "price": 19.99,
        "genre": "Sandbox",
        "rating": 5
    },
    {
        "title": "DayZ",
        "price": 44.99,
        "genre": "Simulation",
        "rating": 3
    }
];

//The genre dropdown and list of genres already added
var genreDropdown = document.getElementById("genreDropdown");
var genres = [];

//Adds all the genres to the dropdown menu
games.forEach(game => {
    if (!genres.includes(game.genre)) {
        var genre = document.createElement("option");
        genre.value = game.genre;
        genre.innerHTML = game.genre;
        genreDropdown.appendChild(genre);
        genres.push(game.genre);
    }
})

//The div for the game list
var gamesDiv = document.getElementById("gameDiv");
gamesDiv.style.display = "flex";
gamesDiv.style.flexDirection = "column";
gamesDiv.style.rowGap = "1em";
gamesDiv.style.padding = "1em";

//Adds all the games to the list
games.forEach(game => {
    //The div for the total game
    var totalDiv = document.createElement("div");
    totalDiv.style.display = "flex";
    totalDiv.style.width = "100%";
    totalDiv.style.height = "3em";
    totalDiv.style.backgroundColor = "darkgrey";
    
    //The button for adding it to your cart
    var cartButton = document.createElement("button");
    cartButton.innerHTML = "Add to cart";
    
    
    //The div for the game name, rating and price
    var gameInfoDiv = document.createElement("div");
    gameInfoDiv.style.marginLeft = "1em";
    gameInfoDiv.style.display = "flex";
    gameInfoDiv.style.width = "100%";
    gameInfoDiv.style.justifyContent = "space-between";

    //The game name paragraph
    var gameName = document.createElement("p");
    gameName.innerHTML = game.title;


    //The game price and rating paragraph
    var gameRatingPrice = document.createElement("p");
    var price = 0;
    var rating = "";
    if (game.price == 0) {
        price = "Free"
    }
    else {
        price = "€" + game.price;
    }

    if(game.rating == 1){
        rating = "star";
    }
    else{
        rating = "stars";
    }
    gameRatingPrice.innerHTML = `${game.rating} ${rating} - ${price}`;
    gameRatingPrice.style.marginRight = "1em";

    //Constructs the game div
    gameInfoDiv.appendChild(gameName)
    gameInfoDiv.appendChild(gameRatingPrice)
    totalDiv.appendChild(cartButton)
    totalDiv.appendChild(gameInfoDiv)

    //Adds the game to the game list
    gamesDiv.appendChild(totalDiv)
})
