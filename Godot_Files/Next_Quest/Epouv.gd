extends KinematicBody2D

var HP = 3000

var tot_timer = 0
var velocity = Vector2()

# Called when the node enters the scene tree for the first time.
var Force_fin = 0
var mini_time = 0
var gra = 3000
var on_screen = false

var Drop_XP = 200
var Drop_pieces = 10
var distance = 0
var spawned = false
var left = false
signal Died

signal Hit_player
var violence = 20
signal Hit

func _ready():
	on_screen = false
	$Body/Arm_1/Cout.hide()
	$Body/Arm_2/Cout2.hide()
	$Body/Eyes.hide()
	$Label.hide()
	$Label.text = str(HP)
	
	var main = get_tree().get_nodes_in_group("Main")
	for node in main:
		self.connect("Died", node, "Ennemy_died")
		self.connect("Hit", node, "Hit")
	var play = get_tree().get_nodes_in_group("Player")
	for node in play:
		self.connect("Hit_player", node, "_on_Epouv_Hit_player")

func _process(delta):
	
	if on_screen and not spawned:
		$AnimationPlayer.play("Spawn")
		$Spawn.playing = true
		
	elif on_screen:
		$AnimationPlayer.play("atk")
		var player = get_tree().get_nodes_in_group("Player")
		var play_pos_x = $"../../../Player/KinematicBody2D".position.x
		distance = position.x - play_pos_x
		if abs(distance) > 5000:
			on_screen = false
			spawned = false
			$Body/Arm_1/Cout.hide()
			$Body/Arm_2/Cout2.hide()
			$Body/Eyes.hide()
		elif abs(distance)<50:
			velocity.x = 0
		elif distance<0:
			if velocity.x < 500:
				velocity.x += 1000*delta
			left = false
		else:
			if velocity.x > -500:
				velocity.x += -1000*delta
			left = true
		$Label.text = str(HP)
		if HP <= 0:
			$Label.hide()
			emit_signal("Died", Drop_XP, Drop_pieces, self.position)
			queue_free()
		
		if Force_fin != 0:
			mini_time += delta
			if mini_time > 0.2:
				emit_signal("Hit", Force_fin, self.position + $Label.rect_position)
				Force_fin = 0
				mini_time = 0
		
		velocity.y += gra*delta
		
		
		velocity = self.move_and_slide(velocity,Vector2(0,-1))
			
			
		if tot_timer < 0.5:
			tot_timer += delta
		elif tot_timer >= 0.5:
			$Label.hide()
		if position.y > 2000:
			queue_free()
	else:
		pass
	


func _on_Player_hit(collider_1, collider_2, collider_3, Force):
	
	tot_timer = 0
	$Label.show()
	if str(self) == collider_1:
		HP -= Force
		Force_fin += Force
		if left:
			velocity.x =500
		else:
			velocity.x =-500
		
	if str(self) == collider_2:
		HP -= Force
		Force_fin += Force
		if left:
			velocity.x =500
		else:
			velocity.x =-500
		
	if str(self) == collider_3:
		HP -= Force
		Force_fin += Force
		if left:
			velocity.x =500
		else:
			velocity.x =-500
	
		
	

func _on_Area2D_body_entered(body):
	emit_signal("Hit_player", violence)
	$hit_enn.playing = true




func _on_VisibilityNotifier2D_screen_entered():
	on_screen = true
	
	$Label.hide()


func _on_AnimationPlayer_animation_finished(anim_name):
	spawned = true
	$Body/Arm_1/Cout.show()
	$Body/Arm_2/Cout2.show()
	$Body/Eyes.show()
