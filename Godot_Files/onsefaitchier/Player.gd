extends KinematicBody2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var velocity = Vector2(200,0)
var gravity = -1200
var jump_force = 750
var jumping = false
var on_ground = true
export var game_over = false
export var score = 0
var high_score = 0
var high_speed = 0

# Called when the node enters the scene tree for the first time.
func _ready():
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	$Label.text = str(int(score))
	$Camera2D/Label3.text = "Vitesse de pénétration actuelle: " + str(int(velocity.x/50)) + " coups/s"
	if score>high_score:
		high_score=score
	if velocity.x/50 > high_speed:
		high_speed = velocity.x/50
	$Camera2D/Label4.text = "Cyclope le plus rapide: " + str(int(high_speed)) + " coups/s"
	$Camera2D/Label2.text = "Bite la plus puissante: " + str(int(high_score))
	jumping = Input.is_action_just_pressed("jumping")
	score += delta*velocity.x/100
	$AnimatedSprite.speed_scale = velocity.x/400
	if jumping and on_ground:
		velocity.y -= jump_force
	
	if velocity.y == 0:
		on_ground = true
	else:
		on_ground = false
	
	velocity += Vector2(delta*60,0)
	velocity.y -= gravity*delta
	velocity = move_and_slide(velocity, Vector2(0, -1), 5, 4, 0.8)
	if position.x > 22000:
		position.x = 0
		position.y = 400
	if velocity.x <= 100:
		game_over = true
		position.x = 0
		position.y = 400
		velocity = Vector2(200,0)
		score = 0
	
