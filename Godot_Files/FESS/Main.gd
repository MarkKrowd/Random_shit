extends Node2D

# class member variables go here, for example:
# var a = 2



func _ready():
	$Node2D.show()
	$Node2D/AnimationPlayer/Sun.show()
	$Node2D/AnimationPlayer/Moon.show()
	$Node2D/AnimationPlayer/Earth.show()
	$Space_Center.hide()
	$Node2D/AnimationPlayer.play("Sun")
	
func _process(delta):
	pass
	





func _on_Quitter_pressed():
	get_tree().quit()


func _on_Nouvelle_partie_pressed():
	$Node2D.hide()
	$Node2D/AnimationPlayer/Sun.hide()
	$Node2D/AnimationPlayer/Moon.hide()
	$Node2D/AnimationPlayer/Earth.hide()
	$Space_Center.show()
	$Music/Main.stop()
	$Music/Space_Center.play()
	$Music/Transition.play()
	
	
	

func _on_Button_pressed():
	$Node2D.show()
	$Node2D/AnimationPlayer/Sun.show()
	$Node2D/AnimationPlayer/Moon.show()
	$Node2D/AnimationPlayer/Earth.show()
	$Space_Center.hide()
	$Music/Main.play()
	$Music/Space_Center.stop()
	$Music/Transition.play()
	
	


func _on_Continuer_pressed():
	$Node2D.hide()
	$Node2D/AnimationPlayer/Sun.hide()
	$Node2D/AnimationPlayer/Moon.hide()
	$Node2D/AnimationPlayer/Earth.hide()
	$Space_Center.show()
	$Music/Main.stop()
	$Music/Space_Center.play()
	$Music/Transition.play()
	
	


func _on_Propagande_pressed():
	$Space_Center/Propagande/Popup/PopupMenu.popup()



func _on_Hangar_pressed():
	$Space_Center/Hangar/Popup2/PopupMenu.popup()


func _on_Lauch_pressed():
	$Space_Center/Launch_Station/Popup3/PopupMenu.popup()
