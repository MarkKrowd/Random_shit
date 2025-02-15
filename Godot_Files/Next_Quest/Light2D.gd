extends Light2D

# Declare member variables here. Examples:
# var a = 2
# var b = "text"
var too_bright = true
var rng = RandomNumberGenerator.new()
var limit_down = 0.75
var limit_up = 1.5
var on_screen = false
# Called when the node enters the scene tree for the first time.
func _ready():
	pass # Replace with function body.

# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta):
	if on_screen:
		if too_bright:
			self.energy -= 0.01
			if self.energy < limit_down:
				too_bright = false
				rng.randomize()
				limit_up = rng.randf_range(1,1.5)
		else:
			self.energy += 0.01
			if self.energy > limit_up:
				too_bright = true
				rng.randomize()
				limit_down = rng.randf_range(0.5,1.2)
	else:
		pass


func _on_VisibilityNotifier2D_screen_entered():
	on_screen = true


func _on_VisibilityNotifier2D_screen_exited():
	on_screen = false
