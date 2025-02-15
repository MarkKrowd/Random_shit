extends KinematicBody2D


export var Type = "Alcolo"

const GRAVITY = 4000
const Frein = 1000

var RECUL = 0
var vit_init = 0
var velocity = Vector2()
var distance = 0
var XP_LOOT = rand_range(1,200)
var HP = rand_range(1,400)
var Just_hitted = false
var Anim_side = ""
var Anim_frappe = false
var Gerbe_time = 0
var Gerbe_son = false

signal died

onready var Gerbe = preload("res://PNJs/Gerbe.tscn")
onready var Gerbe_G = preload("res://PNJs/Gerbe_gauche.tscn")

func _ready():
	# Called when the node is added to the scene for the first time.
	# Initialization here
	var retournement = rand_range(0,20)
	if retournement < 10:
		$AnimatedSprite.flip_h = false
	else:
		$AnimatedSprite.flip_h = true
	if $AnimatedSprite.flip_h:
		$AnimatedSprite.position.x = 115
		
	

func _process(delta):
	var gerber = $AnimatedSprite.frame
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
		
		Gerbe_time+= delta
		if not Gerbe_son:
			$Beger_HARDCORE.play()
			Gerbe_son = true
		if Gerbe_time > 0.06:
			if $AnimatedSprite.flip_h:
				var degueuler = Gerbe.instance()
				add_child(degueuler)
			else:
				var degueuler = Gerbe_G.instance()
				add_child(degueuler)
			Gerbe_time = 0
		velocity = move_and_slide(velocity, Vector2(0, -1))
		
	elif abs(distance) > 1200:
		
		velocity.x = 0
		velocity = move_and_slide(velocity, Vector2(0, -1))
	else:
		if Gerbe_son:
			Gerbe_son = false
		Gerbe_time+= delta
		if Gerbe_time > 3:
			$Beger_normal.play()
			if $AnimatedSprite.flip_h:
				var degueuler = Gerbe.instance()
				add_child(degueuler)
			else:
				var degueuler = Gerbe_G.instance()
				add_child(degueuler)
			Gerbe_time = 0
		if distance >0:
			$AnimatedSprite.flip_h = true
			$AnimatedSprite.position.x = 60
		else:
			$AnimatedSprite.flip_h = false
			$AnimatedSprite.position.x = -60
		
			
		velocity = move_and_slide(velocity, Vector2(0, -1))

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