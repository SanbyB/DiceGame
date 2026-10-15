extends Area2D

@onready var sprite_1: Sprite2D = $flower1
@onready var sprite_2: Sprite2D = $flower2
@onready var sprite_3: Sprite2D = $flower3


@onready var rand: float = randf_range(1, 1.2)

var time: float = 0
var body_colliding: Node2D = null


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	time += delta
	sprite_1.rotation = sin(time*rand)/12
	sprite_2.rotation = sin(time*rand+PI/8)/8
	sprite_3.rotation = sin(time*rand+PI/12)/12
	
	if body_colliding != null:
		sprite_1.rotation += PI/20 * sign((position - body_colliding.position)[0])
		sprite_2.rotation += PI/20 * sign((position - body_colliding.position)[0])
		sprite_3.rotation += PI/20 * sign((position - body_colliding.position)[0])
	

func _on_body_entered(body: Node2D) -> void:
	body_colliding = body
	

func _on_body_exited(body: Node2D) -> void:
	body_colliding = null
