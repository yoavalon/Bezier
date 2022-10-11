d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.position_pen(0,2)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)

d.end()
