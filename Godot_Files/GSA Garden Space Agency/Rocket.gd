extends KinematicBody2D
signal end_flight
export var mass = 0
export var Cx_face = 0.3
export var Surface_face = 0.5
export var Surface_cote = 1
var Cx_cote = 0.6
var rho = 1.225
var thrust = Vector2(0,-1)
var direction = Vector2(0,0)
var rot = Vector2(0,-1)
var trainee = Vector2(0,1)
export var thrust_lenght = 5
var has_fuel = true
export var thrust_power = 20
var Gravity = 981


var on_ground = false
var velocity = Vector2()

var launched = false
var timer = 3
var timer_ended = false
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.


func _process(delta):
	if launched:
		if timer > 0:
			timer-=delta
			if timer<=0:
				timer_ended = true
		if timer_ended:
			rot = rot.normalized()
			if thrust_lenght > 0:
				thrust_lenght -= delta
				if thrust_lenght <=0:
					has_fuel = false
			
			if has_fuel:
				rot.x = rot.x*thrust_power
				rot.y = rot.y*thrust_power
				velocity += rot
				$Textures/Main_1/Main_1.emitting = true
				$Textures/Boost_1/BoostL.emitting = true
				$Textures/Boost_1/BoostL2.emitting = true
			else:
				$Textures/Main_1/Main_1.emitting = false
				$Textures/Boost_1/BoostL.emitting = false
				$Textures/Boost_1/BoostL2.emitting = false
			velocity.y += delta*Gravity
			
			
			
			if on_ground and velocity.y>0:
				velocity.y = 0
				if velocity.x > 0:
					velocity.x = velocity.x/5
					if velocity.x <10:
						velocity.x=0
				elif velocity.x < 0:
					velocity.x = velocity.x/5
					if velocity.x >10:
						velocity.x=0
			if on_ground and velocity.x == 0 and velocity.y == 0 and has_fuel == false:
				emit_signal("end_flight")
				timer_ended = false
				launched = false
			velocity = move_and_slide(velocity,Vector2(0,-1))
	else:
		pass

func _on_Area2D_body_entered(body):
	on_ground = true


func _on_Area2D_body_exited(body):
	on_ground = false


func _on_Launch_butt_pressed():
	launched = true
	timer = 3
	timer_ended = false
	has_fuel = true
	thrust_lenght = 5
	$Launch.play()

func _on_Abort_pressed():
	launched = false
	timer = 3
	timer_ended = false
	emit_signal("end_flight")
