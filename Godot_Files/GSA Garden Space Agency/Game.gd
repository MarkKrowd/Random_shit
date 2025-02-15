extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var launched = false
var launch_timer = 3
var launch_timer_end = false

# Called when the node enters the scene tree for the first time.
func _ready():
	$Deco_1/Deco_1.play("Main")
	$Deco_3/Deco_2.play("Main")
	$Deco_2/Deco_2.play("Main")
	$Static_Buttons/Workshop_butt.hide()
	$Atelier/Atelier.hide()
	$Sounds/Music_1.play()
	$Vaisseau.position.x = 19000
	$Vaisseau.position.y = 900
	$Static_Buttons/Launch_butt.hide()
	$CanvasLayer/Abort.hide()
	
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	var ui_right = Input.is_action_pressed("ui_right")
	var ui_left = Input.is_action_pressed("ui_left")
	
	
	
	if ui_right:
		$CanvasLayer/Left.hide()
	elif ui_left:
		$CanvasLayer/Right.hide()
	elif launched:
		$CanvasLayer/Left.hide()
		$CanvasLayer/Right.hide()
		$Static_Buttons/Launch_butt.hide()
	else:
		$CanvasLayer/Left.show()
		$CanvasLayer/Right.show()
		
	if launched and launch_timer>0 and not launch_timer_end:
		launch_timer-=delta
		if launch_timer <= 0:
			launch_timer_end = true
			$Sounds/Flying.play()
	



func _on_Workshop_body_entered(body):
	$Static_Buttons/Workshop_butt.show()
	

func _on_Workshop_body_exited(body):
	$Static_Buttons/Workshop_butt.hide()
	


func _on_Workshop_butt_pressed():
	$Atelier/Atelier.show()
	$CanvasLayer.scale.y = 10
	$Sounds/Music_1.stop()
	$Sounds/Workshop.play()
	$Sounds/Enter.play()
	$Static_Buttons/Workshop_butt.hide()
	
	
	


func _on_Exit_pressed():
	$Atelier/Atelier.hide()
	$CanvasLayer.scale.y = 1
	$Sounds/Music_1.play()
	$Sounds/Workshop.stop()
	$Sounds/Exit.play()
	$Static_Buttons/Workshop_butt.show()
	
	var Headpos = $Atelier/Atelier.Headpos
	var Accpos = $Atelier/Atelier.Accpos
	var Aeropos = $Atelier/Atelier.Aeropos
	var Mainpos = $Atelier/Atelier.Mainpos
	var Boostpos = $Atelier/Atelier.Boostpos
	
	if Headpos == 1:
		$Vaisseau/Rocket/Textures/Head_1.show()
	else:
		$Vaisseau/Rocket/Textures/Head_1.hide()
		
	if Accpos == 1:
		$Vaisseau/Rocket/Textures/Therm.show()
	else:
		$Vaisseau/Rocket/Textures/Therm.hide()
		
	if Aeropos == 1:
		$Vaisseau/Rocket/Textures/Aero_1.show()
	else:
		$Vaisseau/Rocket/Textures/Aero_1.hide()
		
	if Mainpos == 0:
		$Vaisseau/Rocket/Textures/Main_1.show()
	else:
		$Vaisseau/Rocket/Textures/Main_1.hide()
		
	if Boostpos == 1:
		$Vaisseau/Rocket/Textures/Boost_1.show()
	else:
		$Vaisseau/Rocket/Textures/Boost_1.hide()

	


func _on_Launch_body_entered(body):
	$Static_Buttons/Launch_butt.show()

func _on_Launch_body_exited(body):
	$Static_Buttons/Launch_butt.hide()


func _on_Launch_butt_pressed():
	$Player/KinematicBody2D/Camera2D.current = false
	$Vaisseau/Rocket/Camera2D.current = true
	$CanvasLayer/Left.hide()
	$CanvasLayer/Right.hide()
	$CanvasLayer/Abort.show()
	$HUD/MarginContainer.hide()
	launched = true
	launch_timer = 3
	launch_timer_end = false
	$Sounds/Music_1.stop()


func _on_Abort_pressed():
	$Player/KinematicBody2D/Camera2D.current = true
	$Vaisseau/Rocket/Camera2D.current = false
	$CanvasLayer/Left.show()
	$CanvasLayer/Right.show()
	$CanvasLayer/Abort.hide()
	$HUD/MarginContainer.show()
	launched = false
	$Vaisseau.position.x = 19000
	$Vaisseau.position.y = 890
	launch_timer_end = true
	$Sounds/Flying.stop()
	$Sounds/Music_1.play()

func _on_Rocket_end_flight():
	$Player/KinematicBody2D/Camera2D.current = true
	$Vaisseau/Rocket/Camera2D.current = false
	$CanvasLayer/Left.show()
	$CanvasLayer/Right.show()
	$CanvasLayer/Abort.hide()
	$HUD/MarginContainer.show()
	launched = false
	$Vaisseau.position.x = 19000
	$Vaisseau.position.y = 890
	$Vaisseau/Rocket.position.x = 0
	$Vaisseau/Rocket.position.y = 0
	launch_timer_end = true
	$Sounds/Flying.stop()
	$Sounds/Music_1.play()
