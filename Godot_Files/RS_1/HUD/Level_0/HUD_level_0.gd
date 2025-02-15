extends MarginContainer



onready var life = $Sprite/HP
onready var xp = $Sprite/XP
onready var tween = $Tween

func _ready():
	var player_max_health = $"../../Player/KinematicKevin".max_health
	var player_health = $"../../Player/KinematicKevin".health
	var player_max_xp = $"../../Player/KinematicKevin".Max_XP
	var player_xp = $"../../Player/KinematicKevin".XP
	life.max_value = player_max_health
	life.value = player_health
	xp.max_value = player_max_xp
	xp.value = player_xp
	
	if not tween.is_active():
		tween.start()
	
#func _process(delta):
#	# Called every frame. Delta is time since last frame.
#	# Update game logic here.
#	pass


func _on_KinematicKevin_health_changed(health, max_health):
	update_health(health, max_health)

func update_health(new_value, max_health):
	life.max_value = max_health
	life.value = new_value

func _on_Level_0_Kevin_died():
	var start_color = Color(1.0,1.0,1.0,1.0)
	var end_color = Color(1.0,1.0,1.0,0.0)
	tween.interpolate_property(self,"modulate",start_color,end_color,1.0,Tween.TRANS_LINEAR,Tween.EASE_IN)




func update_xp(XP, XP_Level, Max_XP):
	xp.max_value = Max_XP
	xp.value = XP

func _on_Restart_pressed():
	var XP = $"../../Player/KinematicKevin".XP
	var XP_Level = $"../../Player/KinematicKevin".XP_Level
	var Max_XP = $"../../Player/KinematicKevin".Max_XP
	var player_max_health = $"../../Player/KinematicKevin".max_health
	XP = 0
	update_xp(XP, XP_Level, Max_XP)
	update_health(player_max_health, player_max_health)
	var start_color = Color(1.0,1.0,1.0,0.0)
	var end_color = Color(1.0,1.0,1.0,1.0)
	tween.interpolate_property(self,"modulate",start_color,end_color,1.0,Tween.TRANS_LINEAR,Tween.EASE_IN)



func _on_KinematicKevin_xp_changed(XP, XP_Level, Max_XP):
	update_xp(XP, XP_Level, Max_XP)
