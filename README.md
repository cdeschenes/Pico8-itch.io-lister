<h1>Pico-8 itch.io Game Lister</h1>

<p>A Python script to scrape itch.io for names of games in the Pico-8 categories.</p>

<p><strong>PLEASE NOTE:</strong> This script does not download games; it only collects meta information.</p>

<h2>Goal</h2>
<p>My goal is to make a comprehensive list of (Finished/retail/published) Pico-8 games. Itch.io is a great source of developers publishing games (free/paid) for the Pico-8 platform.</p>

<h2>Usage</h2>
<p>Before running the script, make sure to install the required packages by running the following commands:</p>
<pre>
pip install requests beautifulsoup4
</pre>
<p>Then, execute the script using Python:</p>
<pre>
python itchscrape.py
</pre>

<p>This script will scrape from the <a href="https://itch.io/games/made-with-pico-8">itch.io Pico-8 page</a> and compile a CSV file with the following fields: Game_Name, Game_Price, Game_Genre, and Game_URL.</p>

<p>Example <code>Games_data.csv</code>:</p>
<pre>
1. SUPER CRANE, $5, Puzzle, https://calixjumio.itch.io/super-crane
2. PICOHOT, N/A, Shooter, https://tarkovsky.itch.io/picohot
3. UFO Swamp Odyssey, N/A, Platformer, https://paranoidcactus.itch.io/ufo
4. Villager, N/A, Strategy, https://partnano.itch.io/villager
5. CELESTE Classic, N/A, Platformer, https://mattmakesgames.itch.io/celesteclassic
6. Pico World Race, N/A, Racing, https://pak-9.itch.io/pico-world-race
</pre>

<h2>Ongoing Development</h2>
<p>This is a work in progress, and I hope to add more fields to it in the future to create an organized collection for Pico-8.</p>

<h2>Technical Details</h2>
<p>One of the challenges I came across was the itch.io page loading dynamically when scrolling. To overcome this, the script uses the <code>requests</code> library to fetch the content and <code>BeautifulSoup</code> to parse it. The script loops through all the pages by incrementing <code>page_num</code> until there are no more games to scrape.</p>

<p>Feel free to use and contribute to this project!</p>
