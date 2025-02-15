extends KinematicBody2D

var HP = 10000

var tot_timer = 0
var velocity = Vector2()

# Called when the node enters the scene tree for the first time.
var Force_fin = 0
var mini_time = 0
var gra = 3000

var Drop_XP = 350
var Drop_pieces = 15

signal Died

signal Barde_Mort

signal Hit

func _ready():
	pass

func _process(delta):
	$Label.text = str(HP)
	if HP <= 0:
		emit_signal("Barde_Mort")
		emit_signal("Died", Drop_XP, Drop_pieces, self.position)
		queue_free()
	
	if Force_fin != 0:
		mini_time += delta
		if mini_time > 0.2:
			emit_signal("Hit", Force_fin, self.position + $Label.rect_position)
			Force_fin = 0
			mini_time = 0
	
	velocity.y += gra*delta
	velocity.x = 0
	
	velocity = self.move_and_slide(velocity,Vector2(0,-1))
		
		
	if tot_timer < 0.5:
		tot_timer += delta
	elif tot_timer >= 0.5:
		$Label.hide()
	


func _on_Player_hit(collider_1, collider_2, collider_3, Force):
	tot_timer = 0
	$Label.show()
	if str(self) == collider_1:
		HP -= Force
		Force_fin += Force
		
	if str(self) == collider_2:
		HP -= Force
		Force_fin += Force
		
	if str(self) == collider_3:
		HP -= Force
		Force_fin += Force
	
		
	
