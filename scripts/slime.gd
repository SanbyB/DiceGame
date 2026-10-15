extends CharacterBody2D

@export var dampSpeed: float = 0.93
@export var speed : float = 100
@export var acceleration : float = 1000

var hp: float = 1000
var stunned_time: float = 0

@onready var player = $"../Player"

func _physics_process(_delta):
	var collision = move_and_collide(velocity * _delta)
	if stunned_time <= 0:
		#velocity += acceleration * position.direction_to(player.position) * _delta
		velocity = Vector2(0,0)
	else:
		stunned_time -= _delta
	
	if velocity.length() > speed:
		velocity = velocity.normalized() * speed
	if $AnimatedSprite2D.scale.length() > sqrt(2):
		$AnimatedSprite2D.scale *= 0.98
	#if collision:
		#print("hello")
		## Reflect the velocity vector using the collision normal
		#velocity = velocity.bounce(collision.get_normal())
	if hp <= 0:
		queue_free()
		
	velocity *= dampSpeed
	
	if abs(velocity[0]) < 10:
		velocity[0] = 0
	if abs(velocity[1]) < 10:
		velocity[1] = 0
		
func hit(amount, vel):
	hp -= amount
	print(hp)
	$AnimatedSprite2D.scale = Vector2(2, 2)
	$CPUParticles2D.amount = amount
	$CPUParticles2D.lifetime = amount/50
	$CPUParticles2D.emitting = true
	velocity = vel
	stunned_time = 0.3
	# this is used to stop a collision stick
	position += velocity / 100
