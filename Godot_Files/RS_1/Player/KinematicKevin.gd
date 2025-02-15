extends KinematicBody2D

signal health_changed
signal xp_changed
signal level_up
signal died
signal Shot
signal attacks

export var max_health = 50
export var health = 50
export var XP = 0
export var Max_XP = 100
export var XP_Level = 1
export var Current_strenght = 30

const GRAVITY = 4000
const WALK_SPEED = 300
const RUN_SPEED = 600
const JUMP_FORCE = -1400

var velocity = Vector2()
var on_floor = false
var gravityvar = 2000
var jumping = false
var State = 1
var jump_time = 0.0
var attacking = false
var attack_time = 0
var Ennemi_tapable_D = ""
var Ennemi_tapable_G = ""
var Ennemi_tapable_D2 = ""
var Ennemi_tapable_G2 = ""
var timer_prop = 0
var next_level = true

func _physics_process(delta):
	
	var left = Input.is_action_pressed("ui_left")
	var right = Input.is_action_pressed("ui_right")
	var jump = Input.is_action_just_pressed("ui_accept")
	var walk = Input.is_action_pressed("ui_walk")
	var look_right = Input.is_action_pressed("ui_look_right")
	var look_left = Input.is_action_pressed("ui_look_left")
	var change_direction = Input.is_action_pressed("ui_change_direction")
	var attack = Input.is_action_just_pressed("ui_attack")
	
	if next_level:
		timer_prop += delta
		if timer_prop > 3:
			$Properties.hide()
			timer_prop = 0
			next_level = false
	
	on_floor = $RayCast2D3.is_colliding()
	
	if on_floor:
		gravityvar = 20
	elif not on_floor and not jumping and velocity.y < 0:
		gravityvar = 60000
	else:
		gravityvar = GRAVITY
	
	velocity.y += delta * gravityvar
	if left and right and not jumping:
		velocity.x = 0.0
		
	elif left:
		if not (look_right or look_left):
			if not change_direction:
				$AnimatedSprite.flip_h = true
				$AnimatedSprite.position.x = -53
		if walk:
			velocity.x = -WALK_SPEED
		else:
			velocity.x = -RUN_SPEED
	elif right:
		if not (look_left or look_right):
			if not change_direction:
				$AnimatedSprite.flip_h = false
				$AnimatedSprite.position.x = 65
		if walk:
			velocity.x = WALK_SPEED
		else:
			velocity.x = RUN_SPEED
	else:
		velocity.x = 0
	
		
	
	if velocity.x == 0.0 and on_floor and not jumping:
		velocity.y = 0
	
	if (velocity.x*velocity.x + velocity.y*velocity.y)  > RUN_SPEED*RUN_SPEED and not jumping and on_floor:
		velocity = velocity.normalized() * RUN_SPEED
	
	if on_floor:
		jumping = false
	if jump and on_floor:
		velocity.y = JUMP_FORCE
		jumping = true
		$AudioStreamPlayer.play()
		

	if health <= 0:
		health = 0
		XP = 0
		emit_signal("died")
		State = 0
	
	if attacking:
		$AnimatedSprite.animation = "Attack"
	elif left and right:
		$AnimatedSprite.animation = "Static"
	elif left or right:
		if jumping:
			$AnimatedSprite.animation = "Jump"
		elif not walk:
			$AnimatedSprite.animation = "Run"
		else:
			$AnimatedSprite.animation = "Walk"
	else:
		if jumping:
			$AnimatedSprite.animation = "Jump"
		else:
			$AnimatedSprite.animation = "Static"
			
	
		
	
	velocity = move_and_slide(velocity, Vector2(0, -1), 5, 4, 0.8)
	
	
		
	if attacking:
		attack_time += delta
		if attack_time > 0.25:
			attacking = false
			emit_signal("Shot", Current_strenght)
			attack_time = 0
	if attack:
		$Veuch.play()
		attacking = true
		if $AnimatedSprite.flip_h == false:
			emit_signal("attacks", Current_strenght, Ennemi_tapable_D, Ennemi_tapable_D2, $AnimatedSprite.flip_h)
		else:
			emit_signal("attacks", Current_strenght, Ennemi_tapable_G, Ennemi_tapable_G2, $AnimatedSprite.flip_h)
	

func _on_Level_0_Kevin_died():
	health = 0
	XP = 0
	emit_signal("health_changed", health)


func _on_Restart_pressed():
	health = max_health
	$AnimatedSprite.flip_h = false





func _on_VeuchD_body_entered(body):
	if $AnimatedSprite.flip_h:
		pass
	elif attacking:
		if Ennemi_tapable_D == "":
			Ennemi_tapable_D = str(body)
		else:
			Ennemi_tapable_D2 = str(body)
		emit_signal("attacks", Current_strenght, Ennemi_tapable_D, Ennemi_tapable_D2, $AnimatedSprite.flip_h)
	else:
		if Ennemi_tapable_D == "":
			Ennemi_tapable_D = str(body)
		else:
			Ennemi_tapable_D2 = str(body)

func _on_VeuchD_body_exited(body):
	if Ennemi_tapable_D == str(body):
		Ennemi_tapable_D = ""
	elif Ennemi_tapable_D2 == str(body):
		Ennemi_tapable_D2 = ""


func _on_VeuchG_body_entered(body):
	if not $AnimatedSprite.flip_h:
		pass
	elif attacking:
		if Ennemi_tapable_G == "":
			Ennemi_tapable_G = str(body)
		else:
			Ennemi_tapable_G2 = str(body)
		emit_signal("attacks", Current_strenght, Ennemi_tapable_G,Ennemi_tapable_G2, $AnimatedSprite.flip_h)
	else:
		if Ennemi_tapable_G == "":
			Ennemi_tapable_G = str(body)
		else:
			Ennemi_tapable_G2 = str(body)


func _on_VeuchG_body_exited(body):
	if Ennemi_tapable_G == str(body):
		Ennemi_tapable_G = ""
	elif Ennemi_tapable_G2 == str(body):
		Ennemi_tapable_G2 = ""




func _on_PNJ1_hitted(Force):
	health -= Force
	emit_signal("health_changed", health, max_health)


func _on_PNJ1_died(xp_loot):
	XP += xp_loot
	if XP >= Max_XP:
		while XP>= Max_XP:
			$Level_UP.play()
			Current_strenght+=10
			max_health += 10
			health = max_health
			XP = XP-Max_XP
			XP_Level += 1
			Max_XP = int(Max_XP*1.1)
			emit_signal("health_changed", health, max_health)
			var texte_prop = ("Niveau " + str(XP_Level) + "          HP max: " + str(max_health) + "          Force: " + str(Current_strenght))
			timer_prop = 0
			$Properties.text = texte_prop
			$Properties.show()
			next_level = true
	emit_signal("xp_changed", XP, XP_Level, Max_XP)


func _on_Alcolo_died(xp_loot):
	_on_PNJ1_died(xp_loot)





func _on_Gerbe_collider_body_entered(body):
	if body.Type == "Gerbe":
		$Beger.play()
		health -= 5
		emit_signal("health_changed", health, max_health)
