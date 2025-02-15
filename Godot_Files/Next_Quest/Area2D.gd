extends Area2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	$Sprite.hide()
	self.connect("body_entered", self, "_on_Area2D_body_entered")
	self.connect("body_exited", self, "_on_Area2D_body_exited")
	var play = get_tree().get_nodes_in_group("Player")
	for node in play:
		self.connect("body_entered", node, "_on_Area2D_body_entered")
		self.connect("body_exited", node, "_on_Area2D_body_exited")

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Area2D_body_entered(body):
	$Sprite.show()
	


func _on_Area2D_body_exited(body):
	$Sprite.hide()
