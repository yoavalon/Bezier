d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.position_pen(0,0)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.short)

d.end()
