d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.low)
d.curve(Direction.S, Orient.left, Length.short, Radius.low)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(3,3)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.S, Length.long)

d.end()
