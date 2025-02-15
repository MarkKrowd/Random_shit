extends Node2D


# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var cc = 0
var dist = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass




func _on_CC_text_changed(new_text):
	cc = float(new_text)
	$Res2.text = str(cc*0.16*dist/100)





func _on_Dist_text_changed(new_text):
	dist = float(new_text)
	$Res2.text = str(cc*0.16*dist/100)
