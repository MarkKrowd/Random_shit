extends Node2D

#Headpos 0 = None, 1 = Head_1
export var Headpos = 0
var Headpos_max = 1
#Accpos 0 = None, 1 = Therm
export var Accpos = 0
#warning-ignore:unused_class_variable
var Accpos_max = 1
#Aeropos 0 = None, 1 = Aero_1
export var Aeropos = 0
#warning-ignore:unused_class_variable
var Aeropos_max = 1
#Mainpos 0 = Main_1
export var Mainpos = 0
#warning-ignore:unused_class_variable
var Mainpos_max = 0
#Boostpos 0 = None, 1 = Boos_1
export var Boostpos = 0
#warning-ignore:unused_class_variable
var Boostpos_max = 1



func _ready():
	Headpos = 0
	Accpos = 0
	Aeropos = 0
	Mainpos = 0
	Boostpos = 0
	#choix
	$Choices/Head/None.show()
	$Choices/Head/Head_1.hide()
	$Choices/Accessories/None.show()
	$Choices/Accessories/Therm.hide()
	$Choices/Aerodynamics/None.show()
	$Choices/Aerodynamics/Aero_1.hide()
	$Choices/Main_Engine/Main_1.show()
	$Choices/Boosters/None.show()
	$Choices/Boosters/Boos_1.hide()
	#montage
	


#warning-ignore:unused_argument
func _process(delta):
	#head
	if Headpos == Headpos_max:
		$Buttons/He_Right.hide()
	else:
		$Buttons/He_Right.show()
	if Headpos == 0:
		$Buttons/He_Left.hide()
		$Choices/Head/None.show()
	else:
		$Buttons/He_Left.show()
		$Choices/Head/None.hide()
	if Headpos == 1:
		$Choices/Head/Head_1.show()
		$Mounted/Head/Head_1.show()
	else:
		$Choices/Head/Head_1.hide()
		$Mounted/Head/Head_1.hide()
	
	#accessories
	if Accpos == Accpos_max:
		$Buttons/Ac_Right.hide()
	else:
		$Buttons/Ac_Right.show()
	if Accpos == 0:
		$Buttons/Ac_Left.hide()
		$Choices/Accessories/None.show()
	else:
		$Buttons/Ac_Left.show()
		$Choices/Accessories/None.hide()
	if Accpos == 1:
		$Choices/Accessories/Therm.show()
		$Mounted/Accessories/Therm.show()
	else:
		$Choices/Accessories/Therm.hide()
		$Mounted/Accessories/Therm.hide()
	
	#aerodynamics
	if Aeropos == Aeropos_max:
		$Buttons/Ae_Right.hide()
	else:
		$Buttons/Ae_Right.show()
	if Aeropos == 0:
		$Buttons/Ae_Left.hide()
		$Choices/Aerodynamics/None.show()
	else:
		$Buttons/Ae_Left.show()
		$Choices/Aerodynamics/None.hide()
	if Aeropos == 1:
		$Choices/Aerodynamics/Aero_1.show()
		$Mounted/Aerodynamics/Aero_1.show()
	else:
		$Choices/Aerodynamics/Aero_1.hide()
		$Mounted/Aerodynamics/Aero_1.hide()
	
	#engine
	if Mainpos == Mainpos_max:
		$Buttons/Ma_Right.hide()
	else:
		$Buttons/Ma_Right.show()
	if Mainpos == 0:
		$Buttons/Ma_Left.hide()
		$Choices/Main_Engine/Main_1.show()
		$Mounted/Main_Engine/Main_1.show()
	else:
		$Buttons/Ma_Left.show()
		$Choices/Main_Engine/Main_1.hide()
		$Mounted/Main_Engine/Main_1.hide()
	
	#boosters
	if Boostpos == Boostpos_max:
		$Buttons/Bo_Right.hide()
	else:
		$Buttons/Bo_Right.show()
	if Boostpos == 0:
		$Buttons/Bo_Left.hide()
		$Choices/Boosters/None.show()
	else:
		$Buttons/Bo_Left.show()
		$Choices/Boosters/None.hide()
	if Boostpos == 1:
		$Choices/Boosters/Boos_1.show()
		$Mounted/Boosters/Boos_1.show()
	else:
		$Choices/Boosters/Boos_1.hide()
		$Mounted/Boosters/Boos_1.hide()
	


func _on_He_Left_pressed():
	Headpos -= 1
	$Buttons_sound.play()
func _on_He_Right_pressed():
	Headpos += 1
	$Buttons_sound.play()

func _on_Ac_Left_pressed():
	Accpos -= 1
	$Buttons_sound.play()
func _on_Ac_Right_pressed():
	Accpos += 1
	$Buttons_sound.play()


func _on_Ae_Left_pressed():
	Aeropos -= 1
	$Buttons_sound.play()
func _on_Ae_Right_pressed():
	Aeropos += 1
	$Buttons_sound.play()


func _on_Ma_Left_pressed():
	Mainpos -= 1
	$Buttons_sound.play()
func _on_Ma_Right_pressed():
	Mainpos += 1
	$Buttons_sound.play()


func _on_Bo_Left_pressed():
	Boostpos -= 1
	$Buttons_sound.play()
func _on_Bo_Right_pressed():
	Boostpos += 1
	$Buttons_sound.play()
