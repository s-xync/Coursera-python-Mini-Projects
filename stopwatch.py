import simplegui

# define global variables
time=0
wins=0
used=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(time):
    global t1,time1,time2,t2,time3,t3,ts
    t1=str(time%10)
    time1=time/10
    time2=time1%60
    if time2<10:
        t2='0'+str(time2)
    else:
        t2=str(time2)
    time3=time/600
    t3=str(time3)
    ts=t3+':'+t2+'.'+t1
    return ts
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time=time+1
    
    if time==6001:
        t.stop()
        time=0
        t.start()
    
def  start_timer():
    t.start()
def stop_timer():
    if t.is_running():
        global time,wins,used
        t.stop()
        if time%10==0:
            wins=wins+1
            used=used+1
        else:
            used=used+1
    
def reset_timer():
    global time,wins,used
    time=0
    wins=0
    used=0
    t.stop()

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time),[60,90],50,"Red")
    canvas.draw_text(str(wins)+'/'+str(used),[200,30],25,"Green")
    
    
# create frame
f = simplegui.create_frame('Stop Watch Game',250,150)

# register event handlers
t=simplegui.create_timer(100,tick)
f.set_draw_handler(draw)
f.add_label("Stop the timer at Integral second",150)
f.add_button("Start",start_timer,100)
f.add_button("Stop",stop_timer,100)
f.add_button("Reset",reset_timer,100)


# start frame
f.start()

# Please remember to review the grading rubric
