d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.position_pen(1,3)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.S, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.NE, Length.long)

d.end()
