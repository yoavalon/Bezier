d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)

d.end()
