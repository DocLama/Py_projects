# Fonctionnement
Le chiffre de Beaufort chiffre le texte en utilisant une clé répétée. Pour chaque lettre du texte, on calcule la différence entre la position de la lettre et celle de la lettre correspondante de la clé dans l'alphabet, ce qui donne la lettre chiffrée. Le déchiffrement utilise le même processus, car le chiffre de Beaufort est symétrique.

# Comment Utiliser
L'outil est conçu pour être intuitif :

Au lancement du script, une fenêtre de dialogue vous invite à choisir entre le chiffrement (C) et le déchiffrement (D).
Entrez ensuite le texte que vous souhaitez chiffrer ou déchiffrer.
Fournissez la clé de chiffrement. Cette clé doit être une chaîne de caractères sans espaces ni chiffres.
Le résultat s'affiche dans une nouvelle fenêtre de dialogue, vous montrant le texte chiffré ou déchiffré.
# Avantages
Le chiffre de Beaufort offre une méthode de chiffrement plus sécurisée que le simple chiffre de César, grâce à l'utilisation d'une clé. Cela rend la tâche de déchiffrer le message sans connaître la clé beaucoup plus difficile.

# Interface Graphique
L'utilisation de Tkinter pour l'interface graphique rend notre outil facile à utiliser pour tous, sans avoir besoin de connaissances en ligne de commande. Les interactions se font à travers des boîtes de dialogue simples, guidant l'utilisateur à travers le processus de chiffrement ou de déchiffrement.

