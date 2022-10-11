d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,3)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.high)
d.position_pen(1,2)

d.end()
