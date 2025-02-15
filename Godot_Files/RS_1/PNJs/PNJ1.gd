extends KinematicBody2D

export var Type = "PNJ"
# class member variables go here, for example:
# var a = 2
# var b = "textvar"
const GRAVITY = 4000
var RUN_SPEED = 300
var RECUL = 0
export var Force = 20
var HP = 150
export var XP_LOOT = 50

signal died
signal hitted

var velocity = Vector2()
var distance = 0
var Anim_side = ""
var Anim_frappe = false
var Just_hitted = false

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	RUN_SPEED = rand_range(200,400)

func _process(delta):
	
	var Kevin_position = $"../../Player/KinematicKevin".position
	
	var PNJ_position = position
	if position.y > 1180:
		queue_free()
	velocity.y += GRAVITY * delta
	distance = Kevin_position.x-PNJ_position.x
	
	if Anim_frappe:
		if Anim_side == "Droite":
			if Just_hitted:
				velocity.x = RECUL
				Just_hitted = false
			else:
				velocity.x -= RECUL*delta
				if velocity.x <=0:
					velocity.x = 0
					Anim_frappe = false
					
					
		else:
			if Just_hitted:
				velocity.x = -RECUL
				Just_hitted = false
			else:
				velocity.x += RECUL*delta
				if velocity.x >=0:
					velocity.x = 0
					Anim_frappe = false
					
					
		velocity = move_and_slide(velocity, Vector2(0, -1))
	elif abs(distance) > 800:
		$AnimatedSprite.animation = "Static"
		velocity.x = 0
		velocity = move_and_slide(velocity, Vector2(0, -1))
	else:
		
		if -20<distance and distance<20:
			velocity.x = 0
		elif distance < 0:
			velocity.x = -RUN_SPEED
		else:
			velocity.x = RUN_SPEED
		
		if velocity.x <0:
			$AnimatedSprite.flip_h = true
		else:
			$AnimatedSprite.flip_h = false
		
		velocity = move_and_slide(velocity, Vector2(0, -1))
		if int(velocity.x) == 0:
			$AnimatedSprite.animation = "Static"
		else:
			$AnimatedSprite.animation = "Walk"
		


func _on_KinematicKevin_attacks(Current_strenght, Ennemi_tapable, Ennemi_tapable2, Gauche):
	if str(self) != Ennemi_tapable and str(self) != Ennemi_tapable2:
		pass
	else:
		
		if str(self) != Ennemi_tapable2:
			RECUL = 2000
			
		else:
			RECUL = 1300
			
		Just_hitted = true
		if Gauche:
			Anim_side = "Gauche"
		else:
			Anim_side = "Droite"
		Anim_frappe = true
		HP-=Current_strenght
		if HP<=0:
			emit_signal("died", XP_LOOT)
			queue_free()
		


func _on_Area2D_body_entered(body):
	$AudioStreamPlayer.play()
	emit_signal("hitted", Force)
	
