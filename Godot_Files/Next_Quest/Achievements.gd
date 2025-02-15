extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func _on_Node2D_achievement(text):
	$CanvasLayer/Sprite/Label.text = text
	$CanvasLayer/AnimationPlayer.play("Gotit")
	$CanvasLayer/AudioStreamPlayer.playing = true

func _on_Player_achievment(text):
	$CanvasLayer/Sprite/Label.text = text
	$CanvasLayer/AnimationPlayer.play("Gotit")
	$CanvasLayer/AudioStreamPlayer.playing = true
