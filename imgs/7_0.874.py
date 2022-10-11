d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.short)
d.position_pen(1,3)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.S, Length.medium)

d.end()
