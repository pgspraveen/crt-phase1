class f15:
    def light(self):
        print("ok switch on the light")
    def fan(self,speed):
        print("fan is on and speed is:",speed)
        self.s=speed
    def cpu(self):
        print("powering the system")
        print(self.s)
pgs=f15()
pgs.light()
pgs.fan(6)
pgs.cpu()
    
