extends CharacterBody2D

@export var speed : float = 200
@export var dampSpeed : float = 0.8
@export var acceleration : float = 2000
var sprintSpeed: float = 1000
var dampSprint:float = 0.95
var vel: float = speed
var dice

var Dice = preload("res://scenes/dice.tscn")

var inputDirection : Vector2 = Vector2(0, 0)
var direction = "towards"

var sprint: bool = false

@onready var animatedSprite : AnimatedSprite2D = $PlayerSprite


func get_input():
	inputDirection = Input.get_vector("left", "right", "up", "down")
	sprint = Input.is_action_just_pressed("space")
	if Input.is_action_just_pressed("rightClick") and dice == null:
		var die = Dice.instantiate()
		die.position = get_global_mouse_position()
		## TODO have the dice spawn a specific dist from the player
		get_parent().add_child(die)
		dice = die
	
func move(_delta):
	velocity += inputDirection * acceleration * _delta
	
	if sprint:
		vel = sprintSpeed
	
	if vel > speed:
		vel *= dampSprint
	elif vel < speed:
		vel = speed
	
	if velocity.length() > vel:
		velocity = inputDirection * vel
	
	if inputDirection.length() == 0:
		velocity *= dampSpeed
		
	if abs(velocity[0]) < 10:
		velocity[0] = 0
	if abs(velocity[1]) < 10:
		velocity[1] = 0
		
		
func _physics_process(_delta):
	get_input()
	move(_delta)
	move_and_slide()
	animState(inputDirection)
	


func animState(inputDir):
	if inputDir.length() != 0.0:
		if inputDir[0] < 0:
			direction = "left"
			animatedSprite.flip_h = true
			if inputDir[1] == 0:
				animatedSprite.animation = "walkingTowards"
		elif  inputDir[0] > 0:
			direction = "right"
			animatedSprite.flip_h = false
			if inputDir[1] == 0:
				animatedSprite.animation = "walkingTowards"
		if inputDir[1] > 0:
			animatedSprite.animation = "walkingTowards"
			direction = "towards"
		elif  inputDir[1] < 0:
			direction = "away"
			animatedSprite.animation = "walkingAway"
	
	else:
		match direction:
			"left": animatedSprite.animation = "idleTowards"
			"right": animatedSprite.animation = "idleTowards"
			"towards": animatedSprite.animation = "idleTowards"
			"away": animatedSprite.animation = "idleAway"
