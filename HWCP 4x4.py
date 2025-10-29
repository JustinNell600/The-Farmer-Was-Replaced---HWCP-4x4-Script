clear()
while True:
	for i in range(get_world_size()):
		for i in range(get_world_size()):
			if get_water() < 0.35 or (num_items(Items.Water) >= get_world_size()*get_world_size() and get_water() < 0.75):
				use_item(Items.Water)
			elif can_harvest():
				harvest()
			
			#Colomn 2
			if get_pos_y() == 1:
				if get_pos_x() >= 2:
					if get_ground_type() == Grounds.Grassland:
						till()
						plant(Entities.Carrot)
					plant(Entities.Carrot)
				if get_pos_x() < 2:
					plant(Entities.Tree)
			
			#Colomn 3
			if get_pos_y() == 2:
				if get_ground_type() == Grounds.Grassland:
					till()
					plant(Entities.Pumpkin)
				plant(Entities.Pumpkin)
			
			#Colomn 4
			if get_pos_y() == 3:
				if get_ground_type() == Grounds.Grassland:
					till()
					plant(Entities.Pumpkin)
				plant(Entities.Pumpkin)
				
			move(East)	
		move(North)
		
