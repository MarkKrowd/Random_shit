extends Node2D


# class member variables go here, for example:
# var a = 2
# var b = "textvar"
var died = false
var pause = false
var a = 0
signal Kevin_died

func _ready():
	pass

func _process(delta):
	
	if $Player/KinematicKevin.position.y > 1300:
		emit_signal("Kevin_died")
	
	
	


func _on_Pause_pressed():
	$Pause_screen/Node2D/Button_select.play()
	if died:
		$Pause_screen/Node2D/Label.text = "Vous êtes mort"
	else:
		$Pause_screen/Node2D/Label.text = "Pause"
	if not get_tree().paused:
		get_tree().paused = true
		pause = true
		$Pause_screen/Node2D/MarginContainer/VBoxContainer/Restart.grab_focus()
		$Pause_screen/Node2D.show()
		
	elif get_tree().paused:
		$Pause_screen/Node2D.hide()
		get_tree().paused = false
		pause = false
		


func _on_Restart_pressed():
	$Pause_screen/Node2D/Button_select.play()
	died = false
	get_tree().paused = false
	$Player/KinematicKevin.position = $Spawn.position
	$Pause_screen/Node2D.hide()

func _on_Level_0_Kevin_died():
	died = true
	_on_Pause_pressed()


func _on_KinematicKevin_died():
	_on_Level_0_Kevin_died()


func _on_Quitter_pressed():
	$Pause_screen/Node2D/Button_select.play()
	get_tree().quit()


func _on_Restart_focus_entered():
	$Pause_screen/Node2D/Button.play()


func _on_Options_focus_entered():
	$Pause_screen/Node2D/Button.play()


func _on_Quitter_focus_entered():
	$Pause_screen/Node2D/Button.play()


func _on_Pause_pause():
	_on_Pause_pressed()
