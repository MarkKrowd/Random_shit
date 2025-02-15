extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	var main = get_tree().get_nodes_in_group("Main")
	for node in main:
		$Taverne/Taverne/Taverne/Tavaernier.connect("finished", node, "_on_Tavaernier_finished")
		$Taverne/Taverne/Taverne/Final.connect("finished", node, "_on_Final_finished")
# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
