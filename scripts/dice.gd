extends CharacterBody2D

@export var speed: float = 1000
@export var dampSpeed: float = 0.93
@export var ACCEL: float = 50000
var acceleration: float = ACCEL
var direction: Vector2 = Vector2(0, 0)
var angularVel: float = 0
var dampAngle: float = 0.93
var angleSpeed: float = 3
var max_vel: float = 0

@export var inRange = false
@onready var player = $"../Player"
@onready var animatedSprite = $DiceSprite
var rollNumber = 1

@export var echo_interval: float = 30
@export var echo_lifetime: float = 0.4
@export var echo_color: Color = Color(1.0, 1.0, 1.0, 0.502)

var echo_timer: float = 0.0

func _spawn_echo() -> void:
	var ghost = $DiceSprite.duplicate()
	ghost.top_level = true          # ignore this node's transform from now on
	ghost.modulate = echo_color
	ghost.z_index = animatedSprite.z_index - 1  # draw behind the real sprite
	add_child(ghost)
	ghost.global_transform = animatedSprite.global_transform

	var tween := ghost.create_tween()
	tween.tween_property(ghost, "modulate:a", 0.0, echo_lifetime)
	tween.tween_callback(ghost.queue_free)

	
func _physics_process(_delta):
	velocity += direction * acceleration * _delta
	
	if velocity.length() > speed:
		velocity = direction * speed
	
	if acceleration == 0:
		velocity *= dampSpeed
	
	acceleration = 0
	
		
	if abs(velocity[0]) < 10:
		velocity[0] = 0
	if abs(velocity[1]) < 10:
		velocity[1] = 0
		
	angularVel *= dampAngle
		
	# move_and_collide returns a KinematicCollision2D object if a collision occurs
	var collision = move_and_collide(velocity * _delta)
	
	if collision:
		#TODO
		if collision.get_collider().name == "Slime":
			collision.get_collider().hit(10 * rollNumber, velocity/4)
		# Reflect the velocity vector using the collision normal
		velocity = velocity.bounce(collision.get_normal())
		direction = velocity.normalized()
		acceleration = 0.3 * ACCEL * velocity.length() / max_vel
		
	animState(_delta)
	

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
	angularVel = randf_range(0.5,1) * angleSpeed
	echo_timer = 0
	
	
func animState(delta):
	if inRange:
		animatedSprite.animation = str(rollNumber)
		animatedSprite.play()
	else:
		animatedSprite.stop()
		animatedSprite.animation = "dice"
		animatedSprite.frame = rollNumber - 1
	
	var rot_dir = sign(velocity[0])
	# so the dice always spins
	if rot_dir == 0:
		rot_dir = 1
	animatedSprite.rotate(angularVel * rot_dir)
	max_vel = max(velocity.length(), max_vel)
	if velocity.length() != 0:
		var height_offset: float = abs(cos(PI/2-5*log(velocity.length()/max_vel)))*velocity.length()/12
		animatedSprite.position = Vector2(0, -height_offset-12)
		echo_timer -= delta
		if echo_timer <= 0.0:
			echo_timer = echo_interval/velocity.length()
			_spawn_echo()
	else:
		animatedSprite.position = Vector2(0, -12)
	
		
