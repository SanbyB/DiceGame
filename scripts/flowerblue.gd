extends Node2D

@onready var sprite: Sprite2D = $Sprite2D


@onready var rand: float = randf_range(0.5, 1)

var time: float = 0

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	time += delta
	sprite.rotate(delta * rand)
	var scale = Vector2(sin(time)/3 + 3, sin(time)/3 + 3)
	sprite.scale = scale
	
