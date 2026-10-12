extends CharacterBody2D

@export var speed = 8000
@export var dampSpeed = 0.93
var ACCEL = 50000
var acceleration = ACCEL
var direction = Vector2(0, 0)
var angularVel = 0
var dampAngle = 0.93
var angleSpeed = 5

@export var inRange = false
@onready var player = $"../Player"
@onready var animatedSprite = $DiceSprite
var rollNumber = 1

	
func _physics_process(_delta):
	velocity += direction * acceleration * _delta
	
	if velocity.length() > speed:
		velocity = direction * speed
	
	if acceleration == 0:
		velocity *= dampSpeed
		
	if abs(velocity[0]) < 10:
		velocity[0] = 0
	if abs(velocity[1]) < 10:
		velocity[1] = 0
		
	angularVel *= dampAngle
		
	# move_and_collide returns a KinematicCollision2D object if a collision occurs
	var collision = move_and_collide(velocity * _delta)
	
	if collision:
		# Reflect the velocity vector using the collision normal
		velocity = velocity.bounce(collision.get_normal())
		#TODO
		if collision.get_collider().name == "Slime":
			collision.get_collider().hp -= 50
			print(collision.get_collider().hp)
		
	acceleration = 0
	
	animState()
	

func _on_inrange_area_body_entered(body: Node2D) -> void:
	inRange = true
	

func _on_inrange_area_body_exited(body: Node2D) -> void:
	inRange = false
	

func _on_collideable_area_input_event(viewport: Node, event: InputEvent, shape_idx: int) -> void:
	if event is InputEventMouseButton:
		if event.button_index == MOUSE_BUTTON_LEFT and event.pressed:
			if inRange:
				move()
				return
		if event.button_index == MOUSE_BUTTON_RIGHT and event.pressed:
			if inRange:
				queue_free()

func move():
	velocity = Vector2(0, 0)
	acceleration = ACCEL
	# add the vector of the Node2D transform of position (this is done to ensure draw order)
	direction = player.get_position().direction_to(position + Vector2(0, -12))
	rollNumber = randi_range(1, 6)
	angularVel = randf() * angleSpeed * sign(direction[0])
	
func animState():
	if inRange:
		animatedSprite.animation = str(rollNumber)
		animatedSprite.play()
	else:
		animatedSprite.stop()
		animatedSprite.animation = "dice"
		animatedSprite.frame = rollNumber - 1
	animatedSprite.rotate(angularVel)
