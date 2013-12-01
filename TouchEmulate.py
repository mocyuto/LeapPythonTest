import Tkinter as Tk
from Tkinter import Frame, Canvas, YES, BOTH
import Leap

class TouchPointListener(Leap.Listener):
    def on_init(self, controller):
        print "Initialized"

        self.text = u'test'

    def on_connect(self, controller):
        print "Connected"

        # Enable Gestures
        controller.enable_gesture(Leap.Gesture.TYPE_SWIPE)
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_SCREEN_TAP)
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE)


    def on_frame(self, controller):
        self.paintCanvas.delete("all")
        frame = controller.frame()

        interactionBox = frame.interaction_box

        for pointable in frame.pointables:
            normalizedPosition = interactionBox.normalize_point(pointable.tip_position)
            if(pointable.touch_distance > 0 and pointable.touch_zone != Leap.Pointable.ZONE_NONE):
                color = self.rgb_to_hex((0, 255 - 255 * pointable.touch_distance, 0))

            elif(pointable.touch_distance <= 0):
                color = self.rgb_to_hex((-255 * pointable.touch_distance, 0, 0))
                #color = self.rgb_to_hex((255,0,0))

            else:
                color = self.rgb_to_hex((0,0,200))

            self.draw(normalizedPosition.x * 800, 600 - normalizedPosition.y * 600, 40, 40, color)

        # Gestures
        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                self.text = u'swiping'
                print "now swiping!"
            if gesture.type == Leap.Gesture.TYPE_CIRCLE:
                self.text = u'circling'
        #        self.paintCanvas.create_text('10c','1.5c', text=self.text)
                print "now circling!"
            if gesture.type == Leap.Gesture.TYPE_SCREEN_TAP:
                self.text = "screen tapping!"
         #       self.paintCanvas.create_text('10c','1.5c', text=self.text)
                print "now screen tapping!"
            if gesture.type == Leap.Gesture.TYPE_KEY_TAP:
                self.text = "key tapping!"
          #      self.paintCanvas.create_text('10c','1.5c', text=self.text)
                print "now key tapping!"

    def draw(self, x, y, width, height, color):
        self.paintCanvas.create_text('10c','1.5c', text=self.text)
        self.paintCanvas.create_oval( x, y, x + width, y + height, fill = color, outline = "")

    def set_canvas(self, canvas):
        self.paintCanvas = canvas

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % rgb

class TextMaker(object):
    def __init__(self):
        self.text = u'test'


class PaintBox(Frame):

    def __init__( self ):
        Frame.__init__( self )
        self.leap = Leap.Controller()
        self.painter = TouchPointListener()
        self.leap.add_listener(self.painter)
        self.pack( expand = YES, fill = BOTH )
        self.master.title( "Touch Points" )
        self.master.geometry( "800x600" )

        # create text box
#        cvs = Tk.Canvas(self, text=self.painter.text, width='300', height='50')
 #       cvs.pack()


        # create Canvas component
        self.paintCanvas = Canvas( self, width = "800", height = "600" )
        self.paintCanvas.pack()
        self.painter.set_canvas(self.paintCanvas)

def main():
    PaintBox().mainloop()

if __name__ == "__main__":
    main()
