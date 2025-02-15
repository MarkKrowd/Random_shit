extends Node2D

var speed = 900

var PV = 100
export var PV_max = 100

var gravity = 3000
var presse = false
var eyes_right = true
export var limit_droite = 16000
signal achievment
var distance = Vector2()
var velocity = Vector2()
var direction = Vector2()
var rng = RandomNumberGenerator.new()
var attack = false
var attack_timer = 0
var att_time = 0.4
var Force_fin = 0
var pied = false
var pied_timer = 0
var pi_time = 0.25

var Double_Jumped = false

var playing = false
var actual_zone = 1
signal hit
signal DIED

export var Force = 20


var final_force = Force

export var pied_force = 30

var bat = false
var bat_type = ("null")

signal enter_bat
signal pv_changed
var old_zone = 0
var first_time = true
var occupe = false
signal change_zone

export var achiev_z_one = false

func _ready():
	$KinematicBody2D/AnimationPlayer.play("Static")
	$KinematicBody2D/Body/Bras_G/AvBras_G/Hache/Particles2D.emitting = false
	$KinematicBody2D/Body/Leg_G/Tibia_G/Pied_G/Particles2D.emitting = false
	$KinematicBody2D/Body/Leg_R/Tibia_R/Pied_R/Particles2D2.emitting = false
	
	attack = false
	attack_timer = 0

	pied = false
	pied_timer = 0
	PV = PV_max
	emit_signal("pv_changed", PV, PV_max)
	var ennemies = get_tree().get_nodes_in_group("Ennemies")
	for ennem in ennemies:
		self.connect("hit", ennem, "_on_Player_hit")
	


func _process(delta):
	if occupe:
		$KinematicBody2D/Pas.playing = false
	elif not occupe:
		if first_time:
			first_time = false
		else:
			old_zone = actual_zone
		if $KinematicBody2D.position.x < 64000:
			actual_zone = 1
		elif $KinematicBody2D.position.x < 128000:
			actual_zone = 2
		if $KinematicBody2D/RayCast2D.is_colliding():
			gravity = 0
			Double_Jumped = false
		if old_zone != actual_zone:
			emit_signal("change_zone", actual_zone)
			
		else:
			gravity = 3000
		
		
		direction.x = int(Input.is_action_pressed("ui_right"))-int(Input.is_action_pressed("ui_left"))+int(Input.is_action_pressed("rightc"))-int(Input.is_action_pressed("leftc"))
		var just_right = Input.is_action_just_pressed("ui_right") or Input.is_action_just_pressed("rightc")
		var just_left = Input.is_action_just_pressed("ui_left") or Input.is_action_just_pressed("leftc")
		
		var just_enter = Input.is_action_just_pressed("ui_up") or Input.is_action_just_pressed("enterc")
		if just_enter and bat:
			emit_signal("enter_bat", bat_type)
		
		if direction.x != 0 and $KinematicBody2D/RayCast2D2.is_colliding() and not playing and velocity.x != 0:
			$KinematicBody2D/Pas.playing = true
			playing = true
		elif direction.x == 0 or not $KinematicBody2D/RayCast2D2.is_colliding():
			$KinematicBody2D/Pas.playing = false
			playing = false
		elif velocity.x == 0:
			$KinematicBody2D/Pas.playing = false
			playing = false
		
		var Jump = Input.is_action_just_pressed("Jump") or Input.is_action_just_pressed("jumpc")
		
		var Sneak = Input.is_action_pressed("Slow") or Input.is_action_pressed("slowc")
		
		if Sneak:
			speed = 400
			$KinematicBody2D/AnimationPlayer.playback_speed = 1
			att_time = 0.8
			pi_time = 0.5
			$KinematicBody2D/Pas.pitch_scale = 0.5
			$KinematicBody2D/Sounds/Hu3.pitch_scale = 0.5
		else:
			speed = 900
			$KinematicBody2D/AnimationPlayer.playback_speed = 2
			att_time = 0.4
			pi_time = 0.25
			$KinematicBody2D/Pas.pitch_scale = 0.8
			$KinematicBody2D/Sounds/Hu3.pitch_scale = 1
			
		
		
		
		
		if Jump and $KinematicBody2D/RayCast2D.is_colliding():
			velocity.y = -1300
			Double_Jumped = false
			$KinematicBody2D/Sounds/Hu1.playing = true
		elif Jump and not $KinematicBody2D/RayCast2D.is_colliding() and not Double_Jumped and velocity.y<0:
			Double_Jumped = true
			velocity.y = -1300
			$KinematicBody2D/Sounds/Hu2.playing = true
		
		if just_left and just_right:
			$KinematicBody2D/Pas.playing = false
		elif just_right and not eyes_right:
			
			$KinematicBody2D.scale.x = -0.5
			eyes_right = true
		elif just_left and eyes_right:
			
			$KinematicBody2D.scale.x = -0.5
			eyes_right = false
		
			
		
		if $KinematicBody2D/RayCast2D.is_colliding():
			if direction.x > 0 and $KinematicBody2D.position.x < limit_droite:
				if attack:
					$KinematicBody2D/AnimationPlayer.play("Walking (copy)")
				elif pied:
					$KinematicBody2D/AnimationPlayer.play("Coup pied")
				else:
					if $KinematicBody2D/RayCast2D_R.is_colliding():
						$KinematicBody2D/AnimationPlayer.play("Walk_R")
					elif $KinematicBody2D/RayCast2D_G.is_colliding():
						$KinematicBody2D/AnimationPlayer.play("Walk_G")
					else:
						$KinematicBody2D/AnimationPlayer.play("Walking")
				$KinematicBody2D/Body/Leg_G/Tibia_G/Pied_G/Particles2D.emitting = true
				$KinematicBody2D/Body/Leg_R/Tibia_R/Pied_R/Particles2D2.emitting = true
			elif direction.x < 0 and $KinematicBody2D.position.x >2200:
				if attack:
					$KinematicBody2D/AnimationPlayer.play("Walking (copy)")
				elif pied:
					$KinematicBody2D/AnimationPlayer.play("Coup pied")
				else:
					if $KinematicBody2D/RayCast2D_R.is_colliding():
						$KinematicBody2D/AnimationPlayer.play("Walk_R")
					elif $KinematicBody2D/RayCast2D_G.is_colliding():
						$KinematicBody2D/AnimationPlayer.play("Walk_G")
					else:
						$KinematicBody2D/AnimationPlayer.play("Walking")
				$KinematicBody2D/Body/Leg_G/Tibia_G/Pied_G/Particles2D.emitting = true
				$KinematicBody2D/Body/Leg_R/Tibia_R/Pied_R/Particles2D2.emitting = true
			else:
				if not presse:
					if $KinematicBody2D.position.x > limit_droite:
						emit_signal("achievment", "Putain : Trop pressé!")
						presse = true
				if attack:
					$KinematicBody2D/AnimationPlayer.play("Walking (copy) (copy)")
				elif pied:
					$KinematicBody2D/AnimationPlayer.play("Coup pied")
				else:
					if $KinematicBody2D/RayCast2D_R.is_colliding():
						$KinematicBody2D/AnimationPlayer.play("Static_R")
						
					elif $KinematicBody2D/RayCast2D_G.is_colliding():
						$KinematicBody2D/AnimationPlayer.play("Static_G")
					else:
						$KinematicBody2D/AnimationPlayer.play("Static")
				$KinematicBody2D/Body/Leg_G/Tibia_G/Pied_G/Particles2D.emitting = false
				$KinematicBody2D/Body/Leg_R/Tibia_R/Pied_R/Particles2D2.emitting = false
		
		if direction.x < 0 and $KinematicBody2D.position.x < 2200:
			velocity.x = 0
		elif direction.x > 0 and $KinematicBody2D.position.x >limit_droite:
			velocity.x = 0
		else:
			distance.x = speed
			velocity.x = (direction.x*distance.x)
			
		if not $KinematicBody2D/RayCast2D.is_colliding():
			velocity.y += gravity*delta
		else:
			if not Jump:
				velocity.y = 0
			if direction.x == 0 and not Jump:
				velocity.x = 0
				velocity.y = 0
			else:
				pass
		
		$KinematicBody2D.move_and_slide(velocity,Vector2(0,-1))
		
		if not attack:
			attack = Input.is_action_just_pressed("Click_G") or Input.is_action_just_pressed("CG")
			if attack:
				$KinematicBody2D/Sounds/Hu3.playing = true
		if not pied:
			pied = Input.is_action_just_pressed("Click_D") or Input.is_action_just_pressed("CD")
			if pied:
				$KinematicBody2D/Sounds/Hu4.playing = true
		
		if attack:
			
			pied = false
			$KinematicBody2D/Body/Leg_R/Tibia_R/Pied_R/Particles2D2.emitting = false
			pied_timer = 0
			attack_timer += delta
			$KinematicBody2D/Body/Bras_G/AvBras_G/Hache/Particles2D.emitting = true
			if attack_timer > att_time:
				attack_timer = 0
				attack = false
				$KinematicBody2D/Body/Bras_G/AvBras_G/Hache/Particles2D.emitting = false
		
		elif pied:
			
			attack = false
			attack_timer = 0
			$KinematicBody2D/Body/Bras_G/AvBras_G/Hache/Particles2D.emitting = false
			pied_timer += delta
			$KinematicBody2D/Body/Leg_R/Tibia_R/Pied_R/Particles2D2.emitting = true
			if pied_timer > pi_time:
				pied_timer = 0
				pied = false
				$KinematicBody2D/Body/Leg_R/Tibia_R/Pied_R/Particles2D2.emitting = false
			
		
		
		if not $KinematicBody2D/RayCast2D2.is_colliding():
			if attack:
				if Double_Jumped:
					$KinematicBody2D/AnimationPlayer.play("Attack_Air_Ultra")
				else:
					$KinematicBody2D/AnimationPlayer.play("Attack_Air")
			elif pied:
				$KinematicBody2D/AnimationPlayer.play("Coup pied")
			else:
				$KinematicBody2D/AnimationPlayer.play("Walking")
			$KinematicBody2D/Body/Leg_G/Tibia_G/Pied_G/Particles2D.emitting = false
			$KinematicBody2D/Body/Leg_R/Tibia_R/Pied_R/Particles2D2.emitting = false
		
		hit(attack, pied, Double_Jumped)
		if not attack:
			$KinematicBody2D/Body/Bras_G/AvBras_G/Hache/Particles2D2.emitting = false
			$KinematicBody2D/Sounds/Hit_Hache.playing = false
		if not pied:
			$KinematicBody2D/Body/Leg_R/Tibia_R/Pied_R/Sang.emitting = false
			$KinematicBody2D/Sounds/Hit_Pied.playing = false
		if $KinematicBody2D.position.y > 2000:
			PV = 0
			emit_signal("DIED")
		
		if not achiev_z_one and $KinematicBody2D.position.x > 64000:
			emit_signal("achievment", "Succes: Zone 1 propre")
			achiev_z_one = true
		
	
func hit(attack, pied, D_J):
	if attack:
		var Hache_1 = $KinematicBody2D/Body/Bras_G/AvBras_G/Hache/Hache_1.is_colliding()
		var Hache_2 = $KinematicBody2D/Body/Bras_G/AvBras_G/Hache/Hache_2.is_colliding()
		var Hache_3 = $KinematicBody2D/Body/Bras_G/AvBras_G/Hache/Hache_3.is_colliding()
		rng.randomize()
		var random = rng.randf_range(0.5,2)
		if random > 1.9:
			random = 4
		Force_fin = int(Force * random)
		if D_J:
			final_force = Force_fin*6
		else:
			final_force = Force_fin
		if Hache_1 or Hache_2 or Hache_3:
				if not $KinematicBody2D/Sounds/Hit_Hache.playing:
					$KinematicBody2D/Sounds/Hit_Hache.playing = true
				var collider_1 = $KinematicBody2D/Body/Bras_G/AvBras_G/Hache/Hache_1.get_collider()
				var collider_2 = $KinematicBody2D/Body/Bras_G/AvBras_G/Hache/Hache_2.get_collider()
				var collider_3 = $KinematicBody2D/Body/Bras_G/AvBras_G/Hache/Hache_3.get_collider()
				$KinematicBody2D/Body/Bras_G/AvBras_G/Hache/Particles2D2.emitting = true
				emit_signal("hit", str(collider_1), str(collider_2), str(collider_3), final_force)
		
	if pied:
		rng.randomize()
		var random = rng.randf_range(0.5,2)
		if random > 1.9:
			random = 4
		Force_fin = int(pied_force * random)
		if pied_ok:
			if not $KinematicBody2D/Sounds/Hit_Pied.playing:
				$KinematicBody2D/Sounds/Hit_Pied.playing = true
			var collider_1 = pied_body
			$KinematicBody2D/Body/Leg_R/Tibia_R/Pied_R/Sang.emitting = true
			emit_signal("hit", str(collider_1), "null", "null", Force_fin)
		
			
	




func _on_Area2D_body_entered(body):
	bat = true
	if $KinematicBody2D.position.x < 20000:
		bat_type = ("taverne")
	elif $KinematicBody2D.position.x < 116000:
		bat_type = ("forge")


func _on_Area2D_body_exited(body):
	bat = false
	bat_type = ("null")


func _on_Node2D_in_bat():
	occupe = true


func _on_Node2D_not_in_bat():
	occupe = false




func _on_Node2D_lvl_up(new_PV, new_force):
	PV_max += new_PV
	PV = PV_max
	Force += new_force
	pied_force += new_force
	emit_signal("pv_changed", PV, PV_max)

func save():
	var save_dict = {
		"filename" : "Player",
		"pos_x" : $KinematicBody2D.position.x,
		"pos_y" : $KinematicBody2D.position.y,
		"PV_max" : PV_max,
		"limit_droite" : limit_droite,
		"Force" : Force,
		"pied_force" : pied_force,
		"achiev_z_one": achiev_z_one,
		"actual_zone": actual_zone,
		"old_zone" : 0
		}
	return save_dict

func _on_Node2D_change_pv():
	PV = PV_max
	emit_signal("pv_changed", PV, PV_max)


func _on_Epouv_Hit_player(viol):
	PV -= viol
	if PV <= 0:
		emit_signal("DIED")
	else:
		emit_signal("pv_changed", PV, PV_max)


func _on_Rat_Hit_player(viol):
	PV -= viol
	if PV <= 0:
		emit_signal("DIED")
	else:
		emit_signal("pv_changed", PV, PV_max)

var pied_ok = false
var pied_body = ("")
func _on_Pied_body_entered(body):
	pied_ok = true
	pied_body = body

func _on_Pied_body_exited(body):
	pied_ok = false
	pied_body = ("")


func _on_Node2D_hache_lvl_up():
	Force += 20
	if $KinematicBody2D.position.x < 116000:
		emit_signal("achievment", "Succes: Bulyeah?")
