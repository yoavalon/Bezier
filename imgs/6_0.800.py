d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.SE, Length.short)
d.position_pen(0,0)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.short)

d.end()
