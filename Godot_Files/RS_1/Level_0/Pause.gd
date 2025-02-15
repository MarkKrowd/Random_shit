extends Button

signal pause
# class member variables go here, for example:
# var a = 2
# var b = "textvar"

#func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	#pass

func _process(delta):
	var pause = Input.is_action_just_pressed("ui_pause")
	if pause:
		emit_signal("pause")
