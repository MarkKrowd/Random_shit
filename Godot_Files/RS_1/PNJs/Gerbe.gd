extends RigidBody2D

export var Type = "Gerbe"


var Starting = true
var anim_time = 0
var t_vol_max = 1.5
var t_vol = 0
var pos_y_1 = 0
var pos_y_2 = 0

func _ready():
	$AnimatedSprite.animation = "Start"
	linear_velocity.y = rand_range(-150,0)
	if $AnimatedSprite.flip_h:
		linear_velocity.x = rand_range(600,1000)
		
		position.x = -20
	else:
		position.x = 20
		linear_velocity.x = rand_range(-1000,-600)

func _process(delta):
	if Starting:
		anim_time += delta
		if anim_time > 0.4:
			$AnimatedSprite.animation = "Vol"
			Starting = false
	t_vol += delta
	if t_vol > t_vol_max:
		queue_free()
	
	