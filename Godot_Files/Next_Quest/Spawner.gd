extends VisibilityNotifier2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var Epouv = preload("res://Mobs/Epouv.tscn")
# Called when the node enters the scene tree for the first time.
func _ready():
	self.connect("screen_entered", self, "spawn")

# Called every frame. 'delta' is the elapsed time since the previous frame.
#func _process(delta):
#	pass


func spawn():
	var co = Epouv.instance()
	add_child(co)
	co.pos = self.position + Vector2(1000,0)
	
