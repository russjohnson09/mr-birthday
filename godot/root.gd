extends Node2D


func _on_timer_timeout() -> void:
#	https://docs.godotengine.org/en/latest/tutorials/inputs/handling_quit_requests.html
	get_tree().quit() # default behavior

	pass # Replace with function body.
