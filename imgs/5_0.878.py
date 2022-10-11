d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.NE, Length.medium)

d.end()
