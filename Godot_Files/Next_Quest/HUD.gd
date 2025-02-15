extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
export var Amount_cash = 0
# Called when the node enters the scene tree for the first time.
func _ready():
	old_cash = Amount_cash
	$HUD/Label.text = str(Amount_cash)
	
# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass
var old_cash
signal new

func _on_Node2D_xp_changed(XP, max_XP):
	
	$HUD/XP.max_value = max_XP
	$HUD/XP.value = XP
	$HUD/XP/XP.text = (str(XP)+"/"+str(max_XP))


func _on_Player_pv_changed(PV, PV_max):
	
	$HUD/Life.max_value = PV_max
	$HUD/Life.value = PV
	$HUD/Life/HP.text = (str(PV)+"/"+str(PV_max))


func _on_Node2D_in_bat():
	$HUD/COIN.hide()
	$HUD/Label.hide()
	$HUD/Life.hide()
	$HUD/XP.hide()


func _on_Node2D_not_in_bat():
	$HUD/COIN.show()
	$HUD/Label.show()
	$HUD/Life.show()
	$HUD/XP.show()


func _on_Coin_ramasse():
	Amount_cash += 1
	old_cash = Amount_cash
	$HUD/Label.text = str(Amount_cash)
	
func save():
	var save_dict = {
		"filename" : "HUD",
		"pos_x" : position.x,
		"pos_y" : position.y,
		"Amount_cash" : Amount_cash
		}
	return save_dict

func _on_Node2D_change_pv():
	old_cash = Amount_cash
	$HUD/Label.text = str(Amount_cash)


func _on_Player_DIED():
	Amount_cash = old_cash -10
	$HUD/Label.text = str(Amount_cash)
	if Amount_cash < 0:
		emit_signal("new")
	
