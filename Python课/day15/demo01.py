import time
def story():
    time.sleep(1)
    print("从前有座山")
    print("山里有个庙")
    print("庙里有个老和尚给小和尚讲故事")
    story()
#story()

def fa():
    print("a")
    fb()
def fb():
    print("b")
    fa()
fa()

