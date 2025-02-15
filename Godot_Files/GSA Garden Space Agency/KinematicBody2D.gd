extends KinematicBody2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var eyes_right = true
var velocity = Vector2()
var vitesse_marche = 900

# Called when the node enters the scene tree for the first time.
func _ready():
	$CollisionShape2D/AnimationPlayer.play("Static")


func _process(delta):
	#entrées
	var right = Input.is_action_pressed("ui_right")
	var left = Input.is_action_pressed("ui_left")
	var just_right = Input.is_action_just_pressed("ui_right")
	var just_left = Input.is_action_just_pressed("ui_left")
	
	
	#direction du joueur
	if just_left and just_right:
		pass
	elif just_right and not eyes_right:
		scale.x = -1
		eyes_right = true
	elif just_left and eyes_right:
		scale.x = -1
		eyes_right = false
	
	if just_left or just_right:
		$Walk.play()
	#déplacement joueur
	if left and right:
		velocity.x = 0
		$CollisionShape2D/AnimationPlayer.play("Static")
	elif right:
		velocity.x = vitesse_marche
		$CollisionShape2D/AnimationPlayer.play("Walking")
	elif left:
		velocity.x = -vitesse_marche
		$CollisionShape2D/AnimationPlayer.play("Walking")
	else:
		velocity.x = 0
		$CollisionShape2D/AnimationPlayer.play("Static")
	
	if velocity.x == 0:
		$Walk.stop()
		
	
	
	velocity = move_and_slide(velocity, Vector2(0,-1))
	
	
	
	
	
	
	
	
	
	
	
	
