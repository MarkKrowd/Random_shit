extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var pause = false
var reprendre = false
var started = false
# Called when the node enters the scene tree for the first time.
func _ready():
	$Pause/Fond.hide()
	$Pause/Fond/Options/Fond_options.hide()
	$Pause/Fond/Controles/Fond_binding.hide()
	$Pause/Fond/Controles/bindings.hide()

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var pause_butt = Input.is_action_just_pressed("ui_pause")
	if not started:
		pause_butt = true
		started = true
	
	if pause_butt or reprendre:
		if not pause:
			get_tree().paused = true
			$Pause/Fond.show()
			pause = true
		else:
			get_tree().paused = false
			$Pause/Fond.hide()
			$Pause/Fond/Options/Fond_options.hide()
			$Pause/Fond/Controles/Fond_binding.hide()
			$Pause/Fond/Controles/bindings.hide()
			pause = false
			reprendre = false


func _on_Reprendre_pressed():
	reprendre = true


func _on_Quit_pressed():
	get_tree().quit()


func _on_Nouvelle_pressed():
	var dir = Directory.new()
	dir.remove("user://savegame.save")
	get_tree().paused = false
	get_tree().reload_current_scene()


func _on_Options_pressed():
	$Pause/Fond.hide()
	$Pause/Fond/Options/Fond_options.show()
	if OS.get_screen_count() > 1:
		$Pause/Fond/Options/Fond_options/Ecran1.show()
		$Pause/Fond/Options/Fond_options/Ecran2.show()
	else:
		$Pause/Fond/Options/Fond_options/Ecran1.hide()
		$Pause/Fond/Options/Fond_options/Ecran2.hide()


func _on_Retour_pressed():
	$Pause/Fond.show()
	$Pause/Fond/Options/Fond_options.hide()


func _on_Fullscreen_pressed():
	if OS.is_window_fullscreen():
		OS.set_window_fullscreen(false)
	else:
		OS.set_window_fullscreen(true)


func _on_Ecran1_pressed():
	if OS.is_window_fullscreen():
		OS.set_window_fullscreen(false)
		OS.set_current_screen(0)
		OS.set_window_fullscreen(true)
	else:
		OS.set_current_screen(0)


func _on_Ecran2_pressed():
	if OS.is_window_fullscreen():
		OS.set_window_fullscreen(false)
		OS.set_current_screen(1)
		OS.set_window_fullscreen(true)
	else:
		OS.set_current_screen(1)


func _on_Main_value_changed(value):
	AudioServer.set_bus_volume_db(AudioServer.get_bus_index("Master"), linear2db(value))


func _on_Music_value_changed(value):
	AudioServer.set_bus_volume_db(AudioServer.get_bus_index("Music"), linear2db(value))


func _on_Mobs_value_changed(value):
	AudioServer.set_bus_volume_db(AudioServer.get_bus_index("Mobs"), linear2db(value))


func _on_Controles_pressed():
	$Pause/Fond.hide()
	$Pause/Fond/Controles/Fond_binding.show()
	$Pause/Fond/Controles/bindings.show()


func _on_Retour2_pressed():
	$Pause/Fond.show()
	$Pause/Fond/Controles/Fond_binding.hide()
	$Pause/Fond/Controles/bindings.hide()


func _on_Recommencer_pressed():
	reprendre = true


func _on_HUD_new():
	_on_Nouvelle_pressed()
