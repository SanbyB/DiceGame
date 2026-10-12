extends CharacterBody2D

var hp: float = 100


func _physics_process(_delta):
	var collision = move_and_collide(velocity * _delta)
	if collision:
		# Reflect the velocity vector using the collision normal
		velocity = velocity.bounce(collision.get_normal())
	if hp <= 0:
		queue_free()
