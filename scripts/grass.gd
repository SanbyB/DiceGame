extends Area2D

@onready var sprite_l: Sprite2D = $left
@onready var sprite_r: Sprite2D = $right

@onready var rand: float = randf_range(2.4, 2.7)

var time: float = 0

# Called when the node enters the scene tree for the first time.
func _ready() -> void:
	pass # Replace with function body.


# Called every frame. 'delta' is the elapsed time since the previous frame.
func _process(delta: float) -> void:
	time += delta
	sprite_l.rotation = sin(time*rand)/3
	sprite_r.rotation = sin(time*rand+PI/8)/3
	
