extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var PV_LOSS = preload("res://Perte_PV.tscn")

var LVL_up = preload("res://LVL_UP.tscn")
var Coin = preload("res://Coin.tscn")

var playpos = 0

var rng = RandomNumberGenerator.new()
# Called when the node enters the scene tree for the first time.
func _ready():
	load_game()
	if barde_mort:
		_on_Final_finished()
		$Ennemies/Test/Zone_1/Barde.queue_free()
	emit_signal("xp_changed", XP, max_XP)
	emit_signal("change_pv")

# Called every frame. 'delta' is the elapsed time since the previous frame.

signal change_pv
export var XP = 0
export var max_XP = 100

export var actual_lvl = 1
var gain_PV = 10
var gain_force = 1

export var one = false
signal in_bat
signal not_in_bat

signal achievement
signal xp_changed

signal lvl_up

var pieces = 0
var pos_pieces = Vector2()

export var barde_mort = false

var hache_lvl = 1
signal hache_lvl_up

func _process(delta):
	if pieces>0:
		var co = Coin.instance()
		add_child(co)
		co.pos = pos_pieces
		co.connect("ramasse", $HUD, "_on_Coin_ramasse")
		pieces -= 1
	

func Hit(Force, pos):
	rng.randomize()
	var xxx = rng.randi_range(-100,100)
	rng.randomize()
	var yyy = rng.randi_range(-100,0)
	var PV = PV_LOSS.instance()
	add_child(PV)
	PV.pos = pos+Vector2(0,-40)+Vector2(xxx,yyy)
	PV.txt = (str(Force*-1))
	
	
func level_up():
	actual_lvl += 1
	var new_PV = gain_PV
	var new_force = gain_force
	
	emit_signal("lvl_up", new_PV, new_force)
	var player_pos = $Player/KinematicBody2D.position
	var LVL = LVL_up.instance()
	add_child(LVL)
	LVL.HP = new_PV
	LVL.Force = new_force
	LVL.Actual = actual_lvl
	LVL.pos = player_pos + Vector2(0,-200)


func Ennemy_died(Drop_xp, Drop_Pieces, pos):
	XP += Drop_xp
	while XP > max_XP:
		level_up()
		XP -= max_XP
		max_XP = max_XP * 1.2
		XP = int(XP)
		max_XP = int(max_XP)
	emit_signal("xp_changed", XP, max_XP)
	pieces += Drop_Pieces
	pos_pieces = pos
	

func _on_Barde_Barde_Mort():
	$Music/Z_1_1.playing = true
	barde_mort = true
	emit_signal("achievement", "Succès : Descends-le!")
	


func _on_Barde_Hit(Force, pos):
	Hit(Force, pos)


func _on_Player_enter_bat(bat_type):
	if bat_type == ("taverne"):
		if not one:
			$Background/Zone_1/Taverne/Taverne/Taverne.show()
			$Background/Zone_1/Taverne/Taverne/Taverne/Tavaernier.playing = true
			emit_signal("in_bat")
			$Ennemies/Test/Zone_1/Barde.collision_layer = 6
			$Ennemies/Test/Zone_1/Barde.collision_mask = 6
		elif not barde_mort:
			$Background/Zone_1/Taverne/Taverne/Taverne/Desc.playing = true
		elif barde_mort:
			$Background/Zone_1/Taverne/Taverne/Taverne.show()
			$Background/Zone_1/Taverne/Taverne/Taverne/Final.playing = true
			emit_signal("in_bat")
		else:
			pass
	elif bat_type == ("forge"):
		emit_signal("in_bat")
		$Background/Zone_2/Back_2_3/Forge/CanvasLayer/Forge.show()
		$Background/Zone_2/Back_2_3/Forge/CanvasLayer/Bla.playing = true
	else:
		pass
		


func _on_Tavaernier_finished():
	$Background/Zone_1/Taverne/Taverne/Taverne.hide()
	one = true
	emit_signal("not_in_bat")
	



func _on_Final_finished():
	$Background/Zone_1/Taverne.queue_free()
	$Player.limit_droite = 112000
	emit_signal("not_in_bat")


func _on_Barde_Died(Drop_xp, Drop_Pieces, pos):
	Ennemy_died(Drop_xp, Drop_Pieces, pos)
	
func save_game():
	if $Player/KinematicBody2D.position.x > playpos:
		playpos = $Player/KinematicBody2D.position.x
	var save_game = File.new()
	$Savers/Save.playing = true
	save_game.open("user://savegame.save", File.WRITE)
	var save_nodes = get_tree().get_nodes_in_group("Persist")
	for i in save_nodes:
		var node_data = i.call("save")
		save_game.store_line(to_json(node_data))
	
	save_game.close()
	
	
		
func load_game():
	var save_game = File.new()
	if not save_game.file_exists("user://savegame.save"):
		return
	var line_number = 0
	
	save_game.open("user://savegame.save", File.READ)
	while not save_game.eof_reached():
		if line_number <3:
			
			var current_line  = parse_json(save_game.get_line())
			
				
			var node = current_line["filename"]
			
			if node == "Player":
				$Player/KinematicBody2D.position = Vector2(current_line["pos_x"], current_line["pos_y"])
				for i in current_line.keys():
					if i == "filename" or i == "pos_x" or i == "pos_y":
						continue
					$Player.set(i, current_line[i])
			elif node == "HUD":
				for i in current_line.keys():
					if i == "filename" or i == "pos_x" or i == "pos_y":
						continue
					$HUD.set(i, current_line[i])
			elif node == "Main":
				for i in current_line.keys():
					if i == "filename" or i == "pos_x" or i == "pos_y":
						continue
					set(i, current_line[i])
			line_number += 1
		else:
			var current_line  = parse_json(save_game.get_line())
	save_game.close()
	
	emit_signal("xp_changed", XP, max_XP)
	emit_signal("change_pv")
	
	var Spawners = get_tree().get_nodes_in_group("Ennemies")
	for ennem in Spawners:
		if ennem.position.x < playpos:
			ennem.queue_free()
	change_hache(hache_lvl)
	if hache_lvl >1:
		$Background/Zone_2/Back_2_3/Forge.queue_free()


func _on_Area2D_body_entered(body):
	save_game()


func _on_Recommencer_pressed():
	load_game()

func save():
	var save_dict = {
		"filename" : "Main",
		"pos_x" : position.x,
		"pos_y" : position.y,
		"XP" : XP,
		"max_XP" : max_XP,
		"actual_lvl" : actual_lvl,
		"one" : one,
		"barde_mort": barde_mort,
		"playpos": playpos,
		"hache_lvl": hache_lvl
		}
	return save_dict

func _on_Player_DIED():
	load_game()



func _on_Player_change_zone(new_zone):
	if new_zone == 1:
		if barde_mort:
			$Music/Z_1_1.playing = true
			$Music/Piafs.playing = false
	elif new_zone == 2:
		$Music/Z_1_1.playing = true
		$Music/Piafs.playing = true


func _on_Bla_finished():
	$Background/Zone_2/Back_2_3/Forge.queue_free()
	hache_lvl = 2
	change_hache(hache_lvl)
	emit_signal("hache_lvl_up")
	emit_signal("not_in_bat")
	$Player.limit_droite = 1160000
	
func change_hache(hache):
	if hache == 1:
		$Player/KinematicBody2D/Body/Bras_G/AvBras_G/Hache/LVL1.show()
		$Player/KinematicBody2D/Body/Bras_G/AvBras_G/Hache/LVL2.hide()
	elif hache == 2:
		$Player/KinematicBody2D/Body/Bras_G/AvBras_G/Hache/LVL1.hide()
		$Player/KinematicBody2D/Body/Bras_G/AvBras_G/Hache/LVL2.show()
