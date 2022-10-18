d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.position_pen(0,0)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.position_pen(3,1)
d.straight_line(Direction.S, Length.short)

d.end()
