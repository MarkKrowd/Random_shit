extends KinematicBody2D

var speed = 350
var jump_speed = 900
var gravity = 0


var cont = 0
var text_actual = null
var shield = false
var open_door = false

var distance = Vector2()
var velocity = Vector2()
var direction = Vector2()

func _ready():
	set_physics_process(true)
	set_process(true)
	
	$spr.frame = 3

func _process(delta):
	
	if Input.is_action_just_pressed("ui_select") and open_door:
		$spr.animation = "open_door"
		$spr.playing = true
		yield($spr,"animation_finished")
		print("Bien, has pasado el nivel")
		get_tree().quit()
	
	if $time_shield.is_stopped() == false and $spr.self_modulate.a8 != 100:
		$spr.self_modulate.a8 -= 5
	elif $time_shield.is_stopped() and $spr.self_modulate.a8 != 255:
		$spr.self_modulate.a8 += 5
		shield = false
	
	

func _physics_process(delta):
	_move(delta)


func _move(delta):
	direction.x = int(Input.is_action_pressed("ui_right"))-int(Input.is_action_pressed("ui_left"))
	
	
	
	
		
	
	
	if direction.x > 0:
		$KinematicBody2D.flip_h = false
	elif direction.x < 0:
		$KinematicBody2D.flip_h = true
	
	distance.x = speed*delta
	velocity.x = (direction.x*distance.x)/delta
	velocity.y += gravity*delta
	
	move_and_slide(velocity,Vector2(0,-1))
	
	var get_col = get_slide_collision(get_slide_count()-1)
	
