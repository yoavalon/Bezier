d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)

d.end()
