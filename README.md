# Genetic Algorithm 

### Paramètre du script

<p> Dans le fichier « src.Metier.Parametre_simulation.py », vous pourrez trouver toutes les constantes qui paramètre la simulation :
<ul>
<li>-h, --help : affiche l'aide du script</li>
<li>-r, --reload : recharge le neurone</li>
<li>-l <n>, --learning <n> : lance n seance d'entraînement du neurone</li>
<li>-a, --asking : permet à l'utilisateur de rentrer un nombre et de récuperer la valeur calculée par le neurone</li>
<li>-c, --check : compare les valeurs calculées par le neurone et les valeurs exactes</li>
<li
</ul>
</p>

### Run du script

<p>Pour lancer la simulation, il faut ouvrir une console depuis le dossier genetic_algorithm puis lancer la commande :</p>

<pre><code>pip install matplotlib</code></pre>

<p> Une fois la librairie installée, on peut lancer le script :<p>
	
<pre><code>Python main.py --parameter </code></pre>

### Affichage console et graphe

Pendant l’exécution du script, seul le parametre --check affiche une fenetre avec un graphe. Pour les autres parametres,
l'interaction et l'affichage des informations se font par la console
