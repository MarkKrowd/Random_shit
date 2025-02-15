extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var velocity = Vector2()
var rng = RandomNumberGenerator.new()
var grav = 2000
var statical = false
var pris = false
var pris_timer = 0
signal ramasse
var static_timer = 0

var oui = false

export var pos = Vector2()
# Called when the node enters the scene tree for the first time.
func _ready():
	rng.randomize()
	var xxx = rng.randi_range(-300,300)
	rng.randomize()
	var yyy = rng.randi_range(-1000,-600)
	velocity.x = xxx
	velocity.y = yyy
	

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if not oui:
		$KinematicBody2D.position = pos
		oui = true
	if not pris:
		if not statical:
			velocity.y += grav*delta
			static_timer += delta
			if static_timer >1.5:
				statical = true
			velocity = $KinematicBody2D.move_and_slide(velocity, Vector2(0,-1))
		else:
			pass
			
	else:
		velocity.y -= grav*delta
		
		pris_timer += delta
		velocity = $KinematicBody2D.move_and_slide(velocity, Vector2(0,-1))
		if pris_timer >1:
			queue_free()


func _on_Ramasse_body_entered(body):
	pris = true
	$KinematicBody2D/Piece.playing = true
	emit_signal("ramasse")
