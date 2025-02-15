extends Node2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var speed = 0
var depop_time = 0
export var txt = ("asa")
export var pos = Vector2()

var oui = true
# Called when the node enters the scene tree for the first time.
func _ready():
	pass

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	$Label.text = txt
	if oui:
		$Label.rect_position = pos
		oui = false
	depop_time += delta
	speed += 1000*delta
	$Label.rect_position.y -= speed*delta
	if depop_time > 1:
		queue_free()
