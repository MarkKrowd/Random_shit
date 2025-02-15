extends Node2D


export var HP = 0
export var Force = 0
export var Actual = 1
export var pos = Vector2()

var depop_time = 0
var speed = 0
var oui = false

func _ready():
	pass # Replace with function body.


func _process(delta):
	if not oui:
		$Labels.position = pos
		oui = true
	$Labels/VBoxContainer/Infos.text = ("PV max +" + str(HP))
	$Labels/VBoxContainer/Infos2.text = ("Force +" + str(Force))
	$Labels/VBoxContainer/Infos3.text = ("Niveau actuel:" + str(Actual))
	depop_time += delta
	speed += 75*delta
	$Labels.position.y -= speed*delta
	if depop_time > 3:
		queue_free()
