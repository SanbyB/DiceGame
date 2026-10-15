extends Node2D

@onready var sprite = $Sprite2D
@onready var rand_offset = randf_range(0, PI)

var time:float = 0


# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	time += delta
	sprite.rotation = sin(time*2+rand_offset)/4
