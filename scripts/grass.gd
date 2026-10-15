extends Area2D

@onready var sprite_l: Sprite2D = $left
@onready var sprite_r: Sprite2D = $right

@onready var rand: float = randf_range(2, 2.3)

var time: float = 0

var body_colliding: Node2D = null

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	time += delta
	sprite_l.rotation = sin(time*rand)/3
	sprite_r.rotation = sin(time*rand+PI/8)/3
	if body_colliding != null:
		sprite_l.rotation += PI/12 * sign((position - body_colliding.position)[0])
		sprite_r.rotation += PI/12 * sign((position - body_colliding.position)[0])


func _on_body_entered(body: Node2D) -> void:
	body_colliding = body


func _on_body_exited(body: Node2D) -> void:
	body_colliding = null
