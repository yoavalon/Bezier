d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.long)
d.position_pen(0,2)
d.straight_line(Direction.NW, Length.short)
d.position_pen(3,3)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)

d.end()
