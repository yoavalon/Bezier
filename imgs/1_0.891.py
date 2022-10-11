d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,2)
d.straight_line(Direction.E, Length.long)

d.end()
