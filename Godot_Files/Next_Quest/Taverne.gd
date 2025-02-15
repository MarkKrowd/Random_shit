extends CanvasLayer

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if $Taverne/Tavaernier.playing:
		$Taverne/TXT/Label.text = "Salut jeune voyageur! Bon, je sais bien, comme tout le monde, tu es à la recherche de quêtes. Ta première quête va être extrêmement difficile. Tu entends la musique horrible au loin? C'est notre barde. S'il te plaît, élimine-le!"
		$Taverne/TXT/Label.percent_visible += 0.002
		$Taverne/TXT.position = Vector2(0,918)
	elif $Taverne/Final.playing:
		$Taverne/TXT/Label.text = "Bien! Maintenant que c'est fait, il est temps de passer à une quête un peu plus sérieuse. Et... plus facile surtout. L'île est infestée de monstres et d'autres choses que l'on aime pas trop voir. Si tu pouvais les liquider, ça nous arrangerait. Sache juste que, comme tu as pu voir avec le barde, tu as récupéré quelques pièces. Mais chaque fois que tu mourras, tu perdras 10 pièces. Et si tu n'as plus de pièces, il te faudra tout recommencer. Bonne chance."
		$Taverne/TXT/Label.percent_visible += 0.002
		$Taverne/TXT.position = Vector2(0,780)
	else:
		$Taverne/TXT/Label.percent_visible = 0
