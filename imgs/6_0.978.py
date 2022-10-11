d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(0,1)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)

d.end()
